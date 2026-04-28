#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021806700025838846 | 0.00021886880513961158 | -0.37% | -0.37% | 1.00x | ❌ |
| `get_logger` | 4.872173408932332e-05 | 4.465448913366179e-05 | 8.35% | 9.11% | 1.09x | ✅ |
| `setup_DEBUG2_logging` | 1.1856571640369018e-06 | 1.085250099517768e-06 | 8.47% | 9.25% | 1.09x | ✅ |
