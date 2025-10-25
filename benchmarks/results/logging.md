#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00023737870106374487 | 0.0002385315746733018 | -0.49% | -0.48% | 1.00x | ❌ |
| `get_logger` | 5.287881450592746e-05 | 5.273100494216466e-05 | 0.28% | 0.28% | 1.00x | ✅ |
| `setup_DEBUG2_logging` | 1.1688399317090886e-06 | 1.0744416986067787e-06 | 8.08% | 8.79% | 1.09x | ✅ |
