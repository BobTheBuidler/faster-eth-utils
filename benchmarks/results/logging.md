#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021617597236938847 | 0.00021482726196151908 | 0.62% | 0.63% | 1.01x | ✅ |
| `get_logger` | 4.772589433823551e-05 | 4.430736888544844e-05 | 7.16% | 7.72% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.1802737576732397e-06 | 1.0630789585259742e-06 | 9.93% | 11.02% | 1.11x | ✅ |
