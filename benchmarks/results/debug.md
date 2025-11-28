#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24648964419999403 | 0.2540235759999973 | -3.06% | -2.97% | 0.97x | ❌ |
| `pip_freeze` | 0.24792846199999302 | 0.24504914599998529 | 1.16% | 1.17% | 1.01x | ✅ |
| `platform_info` | 3.2090127387204654e-06 | 3.317830039973289e-06 | -3.39% | -3.28% | 0.97x | ❌ |
| `python_version` | 1.2180790451595562e-06 | 1.2628742173699255e-06 | -3.68% | -3.55% | 0.96x | ❌ |
