#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.31923728280000885 | 0.30904017180000665 | 3.19% | 3.30% | 1.03x | ✅ |
| `pip_freeze` | 0.3024067202000197 | 0.3122264930000028 | -3.25% | -3.15% | 0.97x | ❌ |
| `platform_info` | 3.1407414994367972e-06 | 3.2664677702492413e-06 | -4.00% | -3.85% | 0.96x | ❌ |
| `python_version` | 1.2246094323881126e-06 | 1.1512986314871258e-06 | 5.99% | 6.37% | 1.06x | ✅ |
