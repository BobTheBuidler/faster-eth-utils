#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021347671618531465 | 0.00021460672444337595 | -0.53% | -0.53% | 0.99x | ❌ |
| `get_logger` | 4.732448023283475e-05 | 4.396100734907227e-05 | 7.11% | 7.65% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.329934378702621e-06 | 1.2604789545543345e-06 | 5.22% | 5.51% | 1.06x | ✅ |
