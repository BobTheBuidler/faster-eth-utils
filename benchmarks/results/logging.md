#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002138685442152031 | 0.000219817621796916 | -2.78% | -2.71% | 0.97x | ❌ |
| `get_logger` | 4.78716709620867e-05 | 4.4832651653699406e-05 | 6.35% | 6.78% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.3357303768331298e-06 | 1.331033028748062e-06 | 0.35% | 0.35% | 1.00x | ✅ |
