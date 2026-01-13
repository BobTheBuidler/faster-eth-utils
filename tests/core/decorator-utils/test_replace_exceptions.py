from collections.abc import Callable, Mapping

import pytest

from faster_eth_utils import (
    replace_exceptions,
)


ExceptionMap = Mapping[type[BaseException], type[BaseException]]


@pytest.fixture()
def mock_function_with_exception(
    old_to_new: ExceptionMap,
) -> Callable[[ExceptionMap], None]:
    @replace_exceptions(old_to_new)
    def function_with_exception(x: ExceptionMap) -> None:
        raise TypeError("Boom!")

    return function_with_exception


@pytest.mark.parametrize(
    "old_to_new,new",
    (
        ({TypeError: AttributeError}, AttributeError),
        ({TypeError: NameError}, NameError),
        ({ValueError: AttributeError, TypeError: NameError}, NameError),
    ),
)
def test_decorator_replaces_exceptions(
    mock_function_with_exception: Callable[[ExceptionMap], None],
    old_to_new: ExceptionMap,
    new: type[BaseException],
) -> None:
    with pytest.raises(new, match="Boom!"):
        mock_function_with_exception(old_to_new)
