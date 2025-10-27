#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021001168083842174 | 0.0002096741165193549 | 0.16% | 0.16% | 1.00x | ✅ |
| `get_logger` | 4.762297580167551e-05 | 4.790989052982639e-05 | -0.60% | -0.60% | 0.99x | ❌ |
| `setup_DEBUG2_logging` | 1.2979987915219492e-06 | 1.2105665268990831e-06 | 6.74% | 7.22% | 1.07x | ✅ |
