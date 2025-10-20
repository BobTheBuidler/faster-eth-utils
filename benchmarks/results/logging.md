#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00024145781395989798 | 0.0002463374673822235 | -2.02% | -1.98% | 0.98x | ❌ |
| `get_logger` | 5.2824168628850474e-05 | 5.3208257516134904e-05 | -0.73% | -0.72% | 0.99x | ❌ |
| `setup_DEBUG2_logging` | 1.105080714764128e-06 | 9.991042918207253e-07 | 9.59% | 10.61% | 1.11x | ✅ |
