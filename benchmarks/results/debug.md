#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24745854439998993 | 0.2453082049999921 | 0.87% | 0.88% | 1.01x | ✅ |
| `pip_freeze` | 0.2500521440000057 | 0.24385162160001528 | 2.48% | 2.54% | 1.03x | ✅ |
| `platform_info` | 3.203955808307244e-06 | 3.444520568346164e-06 | -7.51% | -6.98% | 0.93x | ❌ |
| `python_version` | 1.2350827008583825e-06 | 1.4349663354005348e-06 | -16.18% | -13.93% | 0.86x | ❌ |
