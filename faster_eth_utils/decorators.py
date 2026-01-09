import functools
from collections.abc import Callable
from typing import (
    Any,
    Concatenate,
    Final,
    Generic,
    TypeVar,
    final,
)

from typing_extensions import ParamSpec

P = ParamSpec("P")

T = TypeVar("T")

TInstance = TypeVar("TInstance", bound=object)
"""A TypeVar representing an instance that a method can bind to."""


@final
class combomethod(Generic[TInstance, P, T]):
    def __init__(
        self, method: Callable[Concatenate[TInstance | type[TInstance], P], T]
    ) -> None:
        self.method: Final = method

    def __repr__(self) -> str:
        return f"combomethod({self.method})"

    def __get__(
        self,
        obj: TInstance | None,
        objtype: type[TInstance],
    ) -> Callable[P, T]:

        method = self.method
        bound_arg = objtype if obj is None else obj
        
        @functools.wraps(method)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            return method(bound_arg, *args, **kwargs)

        return _wrapper


_return_arg_type_deco_cache: Final[
    dict[int, Callable[[Callable[P, T]], Callable[P, Any]]]
] = {}
# No need to hold so many unique instances in memory


def return_arg_type(at_position: int) -> Callable[[Callable[P, T]], Callable[P, Any]]:
    """
    Wrap the return value with the result of `type(args[at_position])`.
    """
    if deco := _return_arg_type_deco_cache.get(at_position):
        return deco

    def decorator(to_wrap: Callable[P, Any]) -> Callable[P, Any]:
        @functools.wraps(to_wrap)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            result = to_wrap(*args, **kwargs)
            ReturnType = type(args[at_position])
            return ReturnType(result)  # type: ignore [call-arg]

        return wrapper

    _return_arg_type_deco_cache[at_position] = decorator

    return decorator


ExcType = type[BaseException]

ReplaceExceptionsCache = dict[
    tuple[tuple[ExcType, ExcType], ...],
    Callable[[Callable[P, T]], Callable[P, T]],
]

_replace_exceptions_deco_cache: Final[ReplaceExceptionsCache[..., Any]] = {}
# No need to hold so many unique instances in memory


def replace_exceptions(
    old_to_new_exceptions: dict[ExcType, ExcType],
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Replaces old exceptions with new exceptions to be raised in their place.
    """
    cache_key = tuple(old_to_new_exceptions.items())
    if deco := _replace_exceptions_deco_cache.get(cache_key):
        return deco

    old_exceptions = tuple(old_to_new_exceptions)

    def decorator(to_wrap: Callable[P, T]) -> Callable[P, T]:
        @functools.wraps(to_wrap)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
            try:
                return to_wrap(*args, **kwargs)
            except old_exceptions as err:
                try:
                    raise old_to_new_exceptions[type(err)](err) from err
                except KeyError:
                    raise TypeError(
                        f"could not look up new exception to use for {repr(err)}"
                    ) from err

        return wrapped

    _replace_exceptions_deco_cache[cache_key] = decorator

    return decorator
