import functools
import itertools
import os
from typing import (
    Any,
    Callable,
    Dict,
    Final,
    Generic,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    final,
)

from typing_extensions import Concatenate, ParamSpec

P = ParamSpec("P")

T = TypeVar("T")

TInstance = TypeVar("TInstance", bound=object)
"""A TypeVar representing an instance that a method can bind to."""


ExcType = Type[BaseException]

TypedDecorator = Callable[[Callable[P, T]], Callable[P, T]]
UntypedDecorator = Callable[[Callable[P, T]], Callable[P, Any]]

ReplaceExceptionsCacheKey = Tuple[Tuple[ExcType, ExcType], ...]
ReplaceExceptionsCache = Dict[ReplaceExceptionsCacheKey, TypedDecorator[P, T]]

@final
class combomethod(Generic[TInstance, P, T]):
    def __init__(
        self, method: Callable[Concatenate[Union[TInstance, Type[TInstance]], P], T]
    ) -> None:
        self.method: Final = method

    def __repr__(self) -> str:
        return f"combomethod({self.method})"

    def __get__(
        self,
        obj: Optional[TInstance],
        objtype: Type[TInstance],
    ) -> Callable[P, T]:
        
        @functools.wraps(self.method)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            else:
                return self.method(objtype, *args, **kwargs)  # type: ignore [arg-type]

        return _wrapper


_return_arg_type_deco_cache: Final[Dict[int, UntypedDecorator[..., Any]]] = {}
# No need to hold so many unique instances in memory


def return_arg_type(at_position: int) -> UntypedDecorator[P, T]:
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
            return ReturnType(result)  # type: ignore

        return wrapper

    _return_arg_type_deco_cache[at_position] = decorator

    return decorator


_replace_exceptions_deco_cache: Final[ReplaceExceptionsCache[P, T]] = {}
# No need to hold so many unique instances in memory


def replace_exceptions(
    old_to_new_exceptions: Dict[ExcType, ExcType]
) -> TypedDecorator[P, T]:
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
