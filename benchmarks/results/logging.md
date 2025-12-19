#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002143480018835006 | 0.00021579854350027084 | -0.68% | -0.67% | 0.99x | ❌ |
| `get_logger` | 4.799007065407536e-05 | 4.474312583563967e-05 | 6.77% | 7.26% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.3749873753337753e-06 | 1.2807344710601993e-06 | 6.85% | 7.36% | 1.07x | ✅ |
