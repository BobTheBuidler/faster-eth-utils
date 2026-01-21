#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021708292735219344 | 0.0002120132539819451 | 2.34% | 2.39% | 1.02x | ✅ |
| `get_logger` | 5.162434726622206e-05 | 4.5898427850069155e-05 | 11.09% | 12.48% | 1.12x | ✅ |
| `setup_DEBUG2_logging` | 1.446339559780913e-06 | 1.3165551857630793e-06 | 8.97% | 9.86% | 1.10x | ✅ |
