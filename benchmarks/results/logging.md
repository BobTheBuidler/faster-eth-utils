#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021658175915591538 | 0.00021284895616387986 | 1.72% | 1.75% | 1.02x | ✅ |
| `get_logger` | 4.769183516896008e-05 | 4.3623632494567685e-05 | 8.53% | 9.33% | 1.09x | ✅ |
| `setup_DEBUG2_logging` | 1.3845493213384086e-06 | 1.277270505484701e-06 | 7.75% | 8.40% | 1.08x | ✅ |
