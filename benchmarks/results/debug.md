#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24972228099999255 | 0.2498003037999979 | -0.03% | -0.03% | 1.00x | ❌ |
| `pip_freeze` | 0.25416511759999594 | 0.25459764519999906 | -0.17% | -0.17% | 1.00x | ❌ |
| `platform_info` | 3.1924747996775485e-06 | 3.2984945549740356e-06 | -3.32% | -3.21% | 0.97x | ❌ |
| `python_version` | 1.2522141407213027e-06 | 1.4095245571145587e-06 | -12.56% | -11.16% | 0.89x | ❌ |
