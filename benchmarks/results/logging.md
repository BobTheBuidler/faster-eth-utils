#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021263107442636223 | 0.0002147990253472492 | -1.02% | -1.01% | 0.99x | ❌ |
| `get_logger` | 4.829032336546344e-05 | 4.498477749629974e-05 | 6.85% | 7.35% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.278387536598913e-06 | 1.1875214064816814e-06 | 7.11% | 7.65% | 1.08x | ✅ |
