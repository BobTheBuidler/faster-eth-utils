#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002133057293496278 | 0.00021186159082717224 | 0.68% | 0.68% | 1.01x | ✅ |
| `get_logger` | 4.742206699043684e-05 | 4.377215922425494e-05 | 7.70% | 8.34% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.362196768253277e-06 | 1.2634786582281135e-06 | 7.25% | 7.81% | 1.08x | ✅ |
