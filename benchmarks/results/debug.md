#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23429856179999434 | 0.23214662780001163 | 0.92% | 0.93% | 1.01x | ✅ |
| `pip_freeze` | 0.23328000520000386 | 0.2367792247999887 | -1.50% | -1.48% | 0.99x | ❌ |
| `platform_info` | 3.1204505934330022e-06 | 3.620376307468124e-06 | -16.02% | -13.81% | 0.86x | ❌ |
| `python_version` | 1.1866922743822015e-06 | 1.2529034871616987e-06 | -5.58% | -5.28% | 0.95x | ❌ |
