#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24073163559999103 | 0.2376680792000002 | 1.27% | 1.29% | 1.01x | ✅ |
| `pip_freeze` | 0.24223961759997792 | 0.2405797439999901 | 0.69% | 0.69% | 1.01x | ✅ |
| `platform_info` | 2.872622325748367e-06 | 2.8708039265454733e-06 | 0.06% | 0.06% | 1.00x | ✅ |
| `python_version` | 1.198131945436649e-06 | 1.378857940420454e-06 | -15.08% | -13.11% | 0.87x | ❌ |
