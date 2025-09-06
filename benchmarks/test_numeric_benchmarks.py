# mypy: disable-error-code=misc
from typing import Any, Callable

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)

clamp_cases = [
    (0, 10, -5),   # value < lower_bound
    (0, 10, 15),   # value > upper_bound
    (0, 10, 5),    # lower_bound < value < upper_bound
    (0, 10, 0),    # value == lower_bound
    (0, 10, 10),   # value == upper_bound
]

@pytest.mark.benchmark(group="clamp")
@pytest.mark.parametrize("lower,upper,value", clamp_cases)
def test_clamp(benchmark: BenchmarkFixture, lower: int, upper: int, value: int) -> None:
    benchmark(_batch, 10, eth_utils.clamp, lower, upper, value)

@pytest.mark.benchmark(group="clamp")
@pytest.mark.parametrize("lower,upper,value", clamp_cases)
def test_faster_clamp(benchmark: BenchmarkFixture, lower: int, upper: int, value: int) -> None:
    benchmark(_batch, 10, faster_eth_utils.clamp, lower, upper, value)
