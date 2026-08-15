#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002318225190289665 | 0.00022748024928283863 | 1.87% | 1.91% | 1.02x | ✅ |
| `get_logger` | 5.0141240852137916e-05 | 4.707890704939715e-05 | 6.11% | 6.50% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.4450599071126815e-06 | 1.3724777354967361e-06 | 5.02% | 5.29% | 1.05x | ✅ |
