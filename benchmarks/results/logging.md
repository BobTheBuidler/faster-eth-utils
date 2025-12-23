#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002122377788435525 | 0.00021622398245632187 | -1.88% | -1.84% | 0.98x | ❌ |
| `get_logger` | 4.718392678000038e-05 | 4.411815750320685e-05 | 6.50% | 6.95% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.365725091571722e-06 | 1.2872123723631907e-06 | 5.75% | 6.10% | 1.06x | ✅ |
