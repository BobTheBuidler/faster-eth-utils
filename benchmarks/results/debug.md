#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23203450020000674 | 0.23313056279998817 | -0.47% | -0.47% | 1.00x | ❌ |
| `pip_freeze` | 0.2318458931999885 | 0.23140594580002016 | 0.19% | 0.19% | 1.00x | ✅ |
| `platform_info` | 3.0591831557132613e-06 | 3.7139882324872667e-06 | -21.40% | -17.63% | 0.82x | ❌ |
| `python_version` | 1.187514510241243e-06 | 1.3614602496706423e-06 | -14.65% | -12.78% | 0.87x | ❌ |
