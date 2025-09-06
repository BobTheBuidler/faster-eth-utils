# mypy: disable-error-code=misc
from typing import Any, Callable

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils

def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)

keccak_cases = [
    b"hello world",         # bytes
    123456789,              # int
    True,                   # bool
    "0x68656c6c6f",         # hexstr
    "hello world",          # text
    None,                   # invalid (should raise)
    [1, 2, 3],              # invalid (should raise)
]

@pytest.mark.benchmark(group="keccak")
@pytest.mark.parametrize("value", keccak_cases)
def test_keccak(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, eth_utils.keccak, value)

@pytest.mark.benchmark(group="keccak")
@pytest.mark.parametrize("value", keccak_cases)
def test_faster_keccak(benchmark: BenchmarkFixture, value: Any) -> None:
    benchmark(_batch, 10, faster_eth_utils.keccak, value)
