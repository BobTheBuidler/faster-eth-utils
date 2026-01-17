#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021451011082924702 | 0.00021784693179005492 | -1.56% | -1.53% | 0.98x | ❌ |
| `get_logger` | 4.668888654554705e-05 | 4.369620617075063e-05 | 6.41% | 6.85% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.344321486946849e-06 | 1.2632360127716367e-06 | 6.03% | 6.42% | 1.06x | ✅ |
