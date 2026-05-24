#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2551546315999872 | 0.251510776199973 | 1.43% | 1.45% | 1.01x | ✅ |
| `pip_freeze` | 0.2535262452000097 | 0.2551839464000068 | -0.65% | -0.65% | 0.99x | ❌ |
| `platform_info` | 3.0071894153558195e-06 | 3.146129003938124e-06 | -4.62% | -4.42% | 0.96x | ❌ |
| `python_version` | 1.2287302667689506e-06 | 1.1688809830457134e-06 | 4.87% | 5.12% | 1.05x | ✅ |
