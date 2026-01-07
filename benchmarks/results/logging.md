#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00019650495374442517 | 0.00020001273486750055 | -1.79% | -1.75% | 0.98x | ❌ |
| `get_logger` | 4.5100580723461864e-05 | 4.281367154945408e-05 | 5.07% | 5.34% | 1.05x | ✅ |
| `setup_DEBUG2_logging` | 1.1663026035603252e-06 | 1.0523057378811119e-06 | 9.77% | 10.83% | 1.11x | ✅ |
