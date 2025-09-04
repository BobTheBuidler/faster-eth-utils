from typing import Any, Callable

import eth_utils
import pytest
from pytest_codspeed import BenchmarkFixture

import faster_eth_utils


def _batch(i: int, fn: Callable[..., Any], *inputs: Any) -> None:
    for _ in range(i):
        fn(*inputs)


@pytest.mark.benchmark(group="pip_freeze")
def test_pip_freeze(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 1, eth_utils.pip_freeze)


@pytest.mark.benchmark(group="pip_freeze")
def test_faster_pip_freeze(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 1, faster_eth_utils.pip_freeze)


@pytest.mark.benchmark(group="python_version")
def test_python_version(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 10, eth_utils.python_version)


@pytest.mark.benchmark(group="python_version")
def test_faster_python_version(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 10, faster_eth_utils.python_version)


@pytest.mark.benchmark(group="platform_info")
def test_platform_info(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 10, eth_utils.platform_info)


@pytest.mark.benchmark(group="platform_info")
def test_faster_platform_info(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 10, faster_eth_utils.platform_info)


@pytest.mark.benchmark(group="get_environment_summary")
def test_get_environment_summary(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 1, eth_utils.get_environment_summary)


@pytest.mark.benchmark(group="get_environment_summary")
def test_faster_get_environment_summary(benchmark: BenchmarkFixture) -> None:
    benchmark(_batch, 1, faster_eth_utils.get_environment_summary)
