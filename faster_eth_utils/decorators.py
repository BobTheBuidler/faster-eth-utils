from collections.abc import (
    Callable,
    Iterator,
    Sequence,
)
from typing import (
    TypeVar,
)

from .toolz import (
    compose,
    curry,
    reduce,
)


TDecorator = TypeVar("TDecorator", bound=Callable)
TCombomethod = TypeVar("TCombomethod", bound=Callable)
TReturn = TypeVar("TReturn")
TType = TypeVar("TType", bound=type)


def combomethod(f: TCombomethod) -> TCombomethod:
    def _wrap(*args, **kwargs) -> TCombomethod:
        return f(*args, **kwargs)
    _wrap.__doc__ = f.__doc__
    _wrap.__name__ = f.__name__
    return _wrap


def _convert_to_classmethod(f: Callable) -> Callable:
    # Convert combomethod to a classmethod
    return classmethod(f)  # type: ignore[arg-type]


def _convert_to_func(f: Callable) -> Callable:
    # Convert combomethod to a function
    def fn(*args, **kwargs):
        return f(*args, **kwargs)
    fn.__doc__ = f.__doc__
    fn.__name__ = f.__name__
    return fn


def combomethod(fn: TCombomethod) -> TCombomethod:
    def _wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    _wrapper.__doc__ = fn.__doc__
    _wrapper.__name__ = fn.__name__
    return _wrapper


def _convert_to_classmethod(fn: Callable) -> Callable:
    return classmethod(fn)  # type: ignore[arg-type]


def _convert_to_func(fn: Callable) -> Callable:
    def new_fn(*args, **kwargs):
        return fn(*args, **kwargs)
    new_fn.__doc__ = fn.__doc__
    new_fn.__name__ = fn.__name__
    return new_fn


def combomethod(func: Callable[..., object]) -> Callable[..., object]:
    """
    Return a method that can be called as either a class or instance method.
    """
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


def replace_exceptions(
    replacement_errors: tuple[type[Exception], ...] | type[Exception],
    replace_with: type[Exception] = ValidationError,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Replace any of the errors in `replacement_errors` with `replace_with`.
    """
    if isinstance(replacement_errors, type):
        replacement_errors = (replacement_errors,)

    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return fn(*args, **kwargs)
            except replacement_errors as exc:
                raise replace_with from exc

        return wrapper

    return decorator
