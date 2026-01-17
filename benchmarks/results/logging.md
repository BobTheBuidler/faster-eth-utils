#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00022246336631490904 | 0.00021489664389314766 | 3.40% | 3.52% | 1.04x | ✅ |
| `get_logger` | 4.9752586594434336e-05 | 4.6053604531364205e-05 | 7.43% | 8.03% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3496117976997929e-06 | 1.2704118152829174e-06 | 5.87% | 6.23% | 1.06x | ✅ |
