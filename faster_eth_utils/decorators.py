import functools
import itertools
import os
from typing import (
    Any,
    Callable,
    Dict,
    Final,
    Optional,
    Type,
    TypeVar,
    final,
)

from typing_extensions import (
    Concatenate,
    ParamSpec
)

from .types import (
    is_text,
)

T = TypeVar("T")
I = TypeVar("I", bound=object)
# a TypeVar representing an instance that a method can bind to

P = ParamSpec("P")

        
@final
class combomethod(Generic[I, P, T]):
    def __init__(self, method: Callable[Concatenate[I, P], T]) -> None:
        self.method: Final = method

    def __repr__(self) -> str:
        return f"combomethod({self.method})"
    
    def __get__(
        self, obj: Optional[I] = None, objtype: Optional[Type[I]] = None
    ) -> Callable[P, T]:
        @functools.wraps(self.method)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            else:
                return self.method(objtype, *args, **kwargs)  # type: ignore [arg-type]

        return _wrapper


def return_arg_type(at_position: int) -> Callable[..., Callable[..., T]]:
    """
    Wrap the return value with the result of `type(args[at_position])`.
    """

    def decorator(to_wrap: Callable[..., Any]) -> Callable[..., T]:
        @functools.wraps(to_wrap)
        def wrapper(*args: Any, **kwargs: Any) -> T:  # type: ignore
            result = to_wrap(*args, **kwargs)
            ReturnType = type(args[at_position])
            return ReturnType(result)  # type: ignore

        return wrapper

    return decorator


def replace_exceptions(
    old_to_new_exceptions: Dict[Type[BaseException], Type[BaseException]]
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Replaces old exceptions with new exceptions to be raised in their place.
    """
    old_exceptions = tuple(old_to_new_exceptions.keys())

    def decorator(to_wrap: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(to_wrap)
        def wrapped(*args: Any, **kwargs: Any) -> T:
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
