#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.3043877238000164 | 0.2998607761999665 | 1.49% | 1.51% | 1.02x | ✅ |
| `pip_freeze` | 0.31520914200000333 | 0.31090765840000356 | 1.36% | 1.38% | 1.01x | ✅ |
| `platform_info` | 3.2067407406078043e-06 | 3.4159085338182145e-06 | -6.52% | -6.12% | 0.94x | ❌ |
| `python_version` | 1.3091271743415919e-06 | 1.2395578757309066e-06 | 5.31% | 5.61% | 1.06x | ✅ |
