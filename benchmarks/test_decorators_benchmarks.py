import pytest

from faster_eth_utils.decorators import (
    combomethod,
    replace_exceptions,
)


@pytest.mark.benchmark
class TestDecoratorsBenchmarks:
    def test_combomethod(self, benchmark):
        benchmark(combomethod, "foo")

    def test_replace_exceptions(self, benchmark):
        benchmark(replace_exceptions, ValueError)
