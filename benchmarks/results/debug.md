#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2436798874000033 | 0.24269260180001312 | 0.41% | 0.41% | 1.00x | ✅ |
| `pip_freeze` | 0.23969389959999035 | 0.2399925119999807 | -0.12% | -0.12% | 1.00x | ❌ |
| `platform_info` | 3.2026803724110463e-06 | 3.331275481784322e-06 | -4.02% | -3.86% | 0.96x | ❌ |
| `python_version` | 1.2245423223804627e-06 | 1.3894859483828657e-06 | -13.47% | -11.87% | 0.88x | ❌ |
