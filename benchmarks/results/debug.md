#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2295494759999997 | 0.230065703199989 | -0.22% | -0.22% | 1.00x | ❌ |
| `pip_freeze` | 0.22959591600002796 | 0.22895728839999946 | 0.28% | 0.28% | 1.00x | ✅ |
| `platform_info` | 3.0881976585035942e-06 | 3.7233833656749077e-06 | -20.57% | -17.06% | 0.83x | ❌ |
| `python_version` | 1.178486616325944e-06 | 1.2555623257590604e-06 | -6.54% | -6.14% | 0.94x | ❌ |
