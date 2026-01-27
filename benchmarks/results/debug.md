#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.22881569600000376 | 0.22858460260000585 | 0.10% | 0.10% | 1.00x | ✅ |
| `pip_freeze` | 0.2265773623999962 | 0.22737793699999428 | -0.35% | -0.35% | 1.00x | ❌ |
| `platform_info` | 3.075598787166779e-06 | 3.672036492741127e-06 | -19.39% | -16.24% | 0.84x | ❌ |
| `python_version` | 1.1805969715717647e-06 | 1.2646905647399538e-06 | -7.12% | -6.65% | 0.93x | ❌ |
