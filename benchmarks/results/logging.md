#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00022732508034891742 | 0.00022722272226466042 | 0.05% | 0.05% | 1.00x | ✅ |
| `get_logger` | 5.448210536305681e-05 | 5.0597104291828635e-05 | 7.13% | 7.68% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3648933923317451e-06 | 1.2720818613573636e-06 | 6.80% | 7.30% | 1.07x | ✅ |
