#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002246522888124541 | 0.0002252943552118739 | -0.29% | -0.28% | 1.00x | ❌ |
| `get_logger` | 5.2839686770806694e-05 | 5.001398548587058e-05 | 5.35% | 5.65% | 1.06x | ✅ |
| `setup_DEBUG2_logging` | 1.3605165762509925e-06 | 1.2708281079802682e-06 | 6.59% | 7.06% | 1.07x | ✅ |
