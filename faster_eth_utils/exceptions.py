from typing import (
    Any,
)

from .exceptions import (
    ValidationError,
)


class ValidationError(Exception):
    """
    Raised when an invalid value is passed to a function.

    Attributes:
        message (str): explanation of why the error was raised.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class MergeFunctionalityError(Exception):
    """
    Raised when a merge fails due to incompatible data structures.

    Attributes:
        message (str): explanation of why the error was raised.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class ValidationError(Exception):
    """
    Raised when an invalid value is passed to a function.

    Attributes:
        message (str): explanation of why the error was raised.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class MergeFunctionalityError(Exception):
    """
    Raised when a merge fails due to incompatible data structures.

    Attributes:
        message (str): explanation of why the error was raised.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
