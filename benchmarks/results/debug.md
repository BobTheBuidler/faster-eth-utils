#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.29791786579999097 | 0.2985869973999911 | -0.22% | -0.22% | 1.00x | ❌ |
| `pip_freeze` | 0.2995495489999939 | 0.29802130439999247 | 0.51% | 0.51% | 1.01x | ✅ |
| `platform_info` | 3.1512322826359786e-06 | 3.278647165565671e-06 | -4.04% | -3.89% | 0.96x | ❌ |
| `python_version` | 1.2098364664438658e-06 | 1.3609121847511625e-06 | -12.49% | -11.10% | 0.89x | ❌ |
