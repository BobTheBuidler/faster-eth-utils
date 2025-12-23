import contextlib
from functools import (
    cached_property,
)
import logging
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
    overload,
)
from collections.abc import Iterator

from .toolz import (
    assoc,
)

DEBUG2_LEVEL_NUM = 8

TLogger = TypeVar("TLogger", bound=logging.Logger)


class ExtendedDebugLogger(logging.Logger):
    """
    Logging class that can be used for lower level debug logging.
    """

    @cached_property
    def show_debug2(self) -> bool:
        return self.isEnabledFor(DEBUG2_LEVEL_NUM)

    def debug2(self, message: str, *args: Any, **kwargs: Any) -> None:
        if self.show_debug2:
            self.log(DEBUG2_LEVEL_NUM, message, *args, **kwargs)
        else:
            # When we find that `DEBUG2` isn't enabled we completely replace
            # the `debug2` function in this instance of the logger with a noop
            # lambda to further speed up
            self.__dict__["debug2"] = lambda message, *args, **kwargs: None

    def __reduce__(self) -> tuple[Any, ...]:
        # This is needed because our parent's implementation could
        # cause us to become a regular Logger on unpickling.
        return get_extended_debug_logger, (self.name,)


def setup_DEBUG2_logging() -> None:
    """
    Installs the `DEBUG2` level logging levels to the main logging module.
    """
    if not hasattr(logging, "DEBUG2"):
        logging.addLevelName(DEBUG2_LEVEL_NUM, "DEBUG2")
        logging.DEBUG2 = DEBUG2_LEVEL_NUM  # type: ignore [attr-defined]

@contextlib.contextmanager
def _use_logger_class(logger_class: type[logging.Logger]) -> Iterator[None]:
    original_logger_class = logging.getLoggerClass()
    logging.setLoggerClass(logger_class)
    try:
        yield
    finally:
        logging.setLoggerClass(original_logger_class)


@overload
def get_logger(name: str, logger_class: type[TLogger]) -> TLogger: ...
@overload
def get_logger(name: str, logger_class: None = None) -> logging.Logger: ...
def get_logger(name: str, logger_class: Union[type[TLogger], None] = None) -> Union[TLogger, logging.Logger]:
    if logger_class is None:
        return logging.getLogger(name)

    with _use_logger_class(logger_class):
        # The logging module caches logger instances. The following code
        # ensures that if there is a cached instance that we don't
        # accidentally return the incorrect logger type because the logging
        # module does not *update* the cached instance in the event that
        # the global logging class changes.
        manager = logging.Logger.manager
        logger_dict = manager.loggerDict
        cached_logger = logger_dict.get(name)
        if cached_logger is not None and type(cached_logger) is not logger_class:
            del logger_dict[name]
        return cast(TLogger, logging.getLogger(name))


def get_extended_debug_logger(name: str) -> ExtendedDebugLogger:
    return get_logger(name, ExtendedDebugLogger)


THasLoggerMeta = TypeVar("THasLoggerMeta", bound="HasLoggerMeta")


class HasLoggerMeta(type):
    """
    Assigns a logger instance to a class, derived from the import path and name.

    This metaclass uses `__qualname__` to identify a unique and meaningful name
    to use when creating the associated logger for a given class.
    """

    logger_class = logging.Logger

    def __new__(
        mcls: type[THasLoggerMeta],
        name: str,
        bases: tuple[type[Any]],
        namespace: dict[str, Any],
    ) -> THasLoggerMeta:
        if "logger" in namespace:
            # If a logger was explicitly declared we shouldn't do anything to
            # replace it.
            return super().__new__(mcls, name, bases, namespace)
        if "__qualname__" not in namespace:
            raise AttributeError("Missing __qualname__")
    
        logger = get_logger(namespace["__qualname__"], mcls.logger_class)

        return super().__new__(mcls, name, bases, assoc(namespace, "logger", logger))

    @classmethod
    def replace_logger_class(
        mcls: type[THasLoggerMeta], value: type[logging.Logger]
    ) -> type[THasLoggerMeta]:
        return type(mcls.__name__, (mcls,), {"logger_class": value})

    @classmethod
    def meta_compat(
        mcls: type[THasLoggerMeta], other: type[type]
    ) -> type[THasLoggerMeta]:
        return type(mcls.__name__, (mcls, other), {})


class HasLogger(metaclass=HasLoggerMeta):
    logger: logging.Logger


HasExtendedDebugLoggerMeta = HasLoggerMeta.replace_logger_class(ExtendedDebugLogger)


class HasExtendedDebugLogger(metaclass=HasExtendedDebugLoggerMeta):  # type: ignore [metaclass,misc]
    logger: ExtendedDebugLogger
