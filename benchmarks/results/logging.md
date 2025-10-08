#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021373733220933345 | 0.00021375547470143383 | -0.01% | -0.01% | 1.00x | ❌ |
| `get_logger` | 4.757321732873632e-05 | 4.7710290421710093e-05 | -0.29% | -0.29% | 1.00x | ❌ |
| `setup_DEBUG2_logging` | 1.3322738838849328e-06 | 1.2571013114761185e-06 | 5.64% | 5.98% | 1.06x | ✅ |
