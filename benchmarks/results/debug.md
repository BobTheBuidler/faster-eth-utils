#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.29645096399999604 | 0.29476400180000156 | 0.57% | 0.57% | 1.01x | ✅ |
| `pip_freeze` | 0.29335263279999707 | 0.2940558509999846 | -0.24% | -0.24% | 1.00x | ❌ |
| `platform_info` | 2.779089356415377e-06 | 3.1932807190470065e-06 | -14.90% | -12.97% | 0.87x | ❌ |
| `python_version` | 1.0662912710110661e-06 | 1.2430887195861075e-06 | -16.58% | -14.22% | 0.86x | ❌ |
