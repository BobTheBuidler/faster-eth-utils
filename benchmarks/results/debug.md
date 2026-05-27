#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.27238933840000074 | 0.2658874242000138 | 2.39% | 2.45% | 1.02x | ✅ |
| `pip_freeze` | 0.2623652971999945 | 0.2574684294000008 | 1.87% | 1.90% | 1.02x | ✅ |
| `platform_info` | 3.0392382233464927e-06 | 3.298675624213492e-06 | -8.54% | -7.86% | 0.92x | ❌ |
| `python_version` | 1.245840116348114e-06 | 1.3535086377742154e-06 | -8.64% | -7.95% | 0.92x | ❌ |
