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


def return_arg_type(at_position: int) -> Callable[[Callable[P, T]], Callable[P, Any]]:
    """
    Wrap the return value with the result of `type(args[at_position])`.
    """

    def decorator(to_wrap: Callable[P, Any]) -> Callable[P, Any]:
        @functools.wraps(to_wrap)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            result = to_wrap(*args, **kwargs)
            ReturnType = type(args[at_position])
            return ReturnType(result)  # type: ignore

        return wrapper

    return decorator


def replace_exceptions(
    old_to_new_exceptions: Dict[ExcType, ExcType],
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Replaces old exceptions with new exceptions to be raised in their place.
    """
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

    return decorator
