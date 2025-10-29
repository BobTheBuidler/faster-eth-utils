#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.29692374140001904 | 0.29484155000002377 | 0.70% | 0.71% | 1.01x | ✅ |
| `pip_freeze` | 0.29650561600001313 | 0.2945866866000074 | 0.65% | 0.65% | 1.01x | ✅ |
| `platform_info` | 3.2013958344290216e-06 | 3.315310731563582e-06 | -3.56% | -3.44% | 0.97x | ❌ |
| `python_version` | 1.2333946443180375e-06 | 1.4243016765992862e-06 | -15.48% | -13.40% | 0.87x | ❌ |
