#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00019678727276955672 | 0.00019728672282524282 | -0.25% | -0.25% | 1.00x | ❌ |
| `get_logger` | 4.5643060807088257e-05 | 4.3198038075029703e-05 | 5.36% | 5.66% | 1.06x | ✅ |
| `setup_DEBUG2_logging` | 1.17163681558846e-06 | 1.033062195353093e-06 | 11.83% | 13.41% | 1.13x | ✅ |
