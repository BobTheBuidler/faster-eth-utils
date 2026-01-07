#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.000214030556246991 | 0.0002123492315385023 | 0.79% | 0.79% | 1.01x | ✅ |
| `get_logger` | 4.8851164194921945e-05 | 4.5134828484563124e-05 | 7.61% | 8.23% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3761529827387279e-06 | 1.384161819759948e-06 | -0.58% | -0.58% | 0.99x | ❌ |
