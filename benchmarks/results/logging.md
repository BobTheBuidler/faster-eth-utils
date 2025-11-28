#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002186619909140122 | 0.0002217489963313737 | -1.41% | -1.39% | 0.99x | ❌ |
| `get_logger` | 4.992853397047041e-05 | 4.608001894859329e-05 | 7.71% | 8.35% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3122551079380117e-06 | 1.2254017644759728e-06 | 6.62% | 7.09% | 1.07x | ✅ |
