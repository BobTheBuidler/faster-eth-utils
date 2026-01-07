#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2733592138000063 | 0.2778367737999929 | -1.64% | -1.61% | 0.98x | ❌ |
| `pip_freeze` | 0.26231345759998703 | 0.2714188618000094 | -3.47% | -3.35% | 0.97x | ❌ |
| `platform_info` | 3.090254120172256e-06 | 3.4697694726848092e-06 | -12.28% | -10.94% | 0.89x | ❌ |
| `python_version` | 1.1851708498543517e-06 | 1.2939458147208966e-06 | -9.18% | -8.41% | 0.92x | ❌ |
