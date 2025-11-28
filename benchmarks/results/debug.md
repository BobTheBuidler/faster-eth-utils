#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23974539979999462 | 0.24222752119999313 | -1.04% | -1.02% | 0.99x | ❌ |
| `pip_freeze` | 0.24114924279999742 | 0.24048063400000502 | 0.28% | 0.28% | 1.00x | ✅ |
| `platform_info` | 3.2017388536825044e-06 | 3.3282389570419314e-06 | -3.95% | -3.80% | 0.96x | ❌ |
| `python_version` | 1.2000811625109796e-06 | 1.2656700760639075e-06 | -5.47% | -5.18% | 0.95x | ❌ |
