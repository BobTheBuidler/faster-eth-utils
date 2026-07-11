#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.27314078959998367 | 0.27145037359999835 | 0.62% | 0.62% | 1.01x | ✅ |
| `pip_freeze` | 0.26799151000001303 | 0.2689236806000054 | -0.35% | -0.35% | 1.00x | ❌ |
| `platform_info` | 2.8097702489565334e-06 | 2.883480650505829e-06 | -2.62% | -2.56% | 0.97x | ❌ |
| `python_version` | 1.0924793235968342e-06 | 1.323603428704425e-06 | -21.16% | -17.46% | 0.83x | ❌ |
