# mypy: disable-error-code=misc
from typing import Any, Callable, Tuple

import eth_utils
import eth_utils.decorators
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils
import faster_eth_utils.decorators

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)


# return_arg_type: test with int, str, float, at_position 0 and 1
rat_cases = [
    (0, (1, 2)),         # int, at position 0
    (1, (1, 2)),         # int, at position 1
    (0, ("a", "b")),     # str, at position 0
    (1, ("a", "b")),     # str, at position 1
    (0, (1.5, 2.5)),     # float, at position 0
]

# replace_exceptions: mapped, unmapped, no exception
def raise_value_error():
    raise ValueError("fail")

def raise_type_error():
    raise TypeError("fail")

def no_raise():
    return 42

re_cases = [
    (raise_value_error, {ValueError: RuntimeError}),  # mapped
    (raise_type_error, {ValueError: RuntimeError}),   # unmapped (should raise TypeError)
    (no_raise, {ValueError: RuntimeError}),           # no exception
]

@pytest.mark.benchmark(group="return_arg_type")
@pytest.mark.parametrize("at_position,args", rat_cases)
def test_return_arg_type(
    benchmark: BenchmarkFixture,
    at_position: int,
    args: Tuple[Any, ...]
) -> None:
    def add(x: Any, y: Any) -> Any:
        return x + y
    decorated = eth_utils.decorators.return_arg_type(at_position)(add)
    benchmark(_batch, 10, decorated, *args)

@pytest.mark.benchmark(group="return_arg_type")
@pytest.mark.parametrize("at_position,args", rat_cases)
def test_faster_return_arg_type(
    benchmark: BenchmarkFixture,
    at_position: int,
    args: Tuple[Any, ...]
) -> None:
    def add(x: Any, y: Any) -> Any:
        return x + y
    decorated = faster_eth_utils.decorators.return_arg_type(at_position)(add)
    benchmark(_batch, 10, decorated, *args)

@pytest.mark.benchmark(group="replace_exceptions")
@pytest.mark.parametrize("fn,exc_map", re_cases)
def test_replace_exceptions(
    benchmark: BenchmarkFixture,
    fn: Callable[[], Any],
    exc_map: dict
) -> None:
    decorated = eth_utils.replace_exceptions(exc_map)(fn)
    try:
        benchmark(_batch, 10, decorated)
    except Exception:
        pass

@pytest.mark.benchmark(group="replace_exceptions")
@pytest.mark.parametrize("fn,exc_map", re_cases)
def test_faster_replace_exceptions(
    benchmark: BenchmarkFixture,
    fn: Callable[[], Any],
    exc_map: dict
) -> None:
    decorated = faster_eth_utils.replace_exceptions(exc_map)(fn)
    try:
        benchmark(_batch, 10, decorated)
    except Exception:
        pass
