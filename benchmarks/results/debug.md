#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2260336389999793 | 0.22654253540001718 | -0.23% | -0.22% | 1.00x | ❌ |
| `pip_freeze` | 0.22639699220001147 | 0.22595294760001253 | 0.20% | 0.20% | 1.00x | ✅ |
| `platform_info` | 3.0616755043870444e-06 | 3.506816153548483e-06 | -14.54% | -12.69% | 0.87x | ❌ |
| `python_version` | 1.1797474661448002e-06 | 1.2095676146686458e-06 | -2.53% | -2.47% | 0.98x | ❌ |
