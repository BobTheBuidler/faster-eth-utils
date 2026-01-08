#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2502113494000014 | 0.24770580480000035 | 1.00% | 1.01% | 1.01x | ✅ |
| `pip_freeze` | 0.2618707843999914 | 0.2501798334 | 4.46% | 4.67% | 1.05x | ✅ |
| `platform_info` | 3.1559564063370967e-06 | 3.4208777695568766e-06 | -8.39% | -7.74% | 0.92x | ❌ |
| `python_version` | 1.1715227879453444e-06 | 1.181863748871238e-06 | -0.88% | -0.87% | 0.99x | ❌ |
