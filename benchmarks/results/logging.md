#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00022274447077649096 | 0.00022594478629443893 | -1.44% | -1.42% | 0.99x | ❌ |
| `get_logger` | 4.7767518407136905e-05 | 4.438813906825772e-05 | 7.07% | 7.61% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3138347688580109e-06 | 1.2254894823180104e-06 | 6.72% | 7.21% | 1.07x | ✅ |
