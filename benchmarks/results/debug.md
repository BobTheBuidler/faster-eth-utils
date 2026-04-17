#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.26104025619999904 | 0.26753744879999886 | -2.49% | -2.43% | 0.98x | ❌ |
| `pip_freeze` | 0.26698928799999067 | 0.2580350775999932 | 3.35% | 3.47% | 1.03x | ✅ |
| `platform_info` | 2.8478064089969205e-06 | 3.3876684977417562e-06 | -18.96% | -15.94% | 0.84x | ❌ |
| `python_version` | 1.112854855019379e-06 | 1.4079676913416538e-06 | -26.52% | -20.96% | 0.79x | ❌ |
