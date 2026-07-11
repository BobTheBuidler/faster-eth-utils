#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002150440249738389 | 0.0002131979390979633 | 0.86% | 0.87% | 1.01x | ✅ |
| `get_logger` | 4.821973219734747e-05 | 4.507588211603174e-05 | 6.52% | 6.97% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.1823124225495538e-06 | 1.0974175839631506e-06 | 7.18% | 7.74% | 1.08x | ✅ |
