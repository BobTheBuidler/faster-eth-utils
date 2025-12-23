#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2428599360000021 | 0.24090425320000577 | 0.81% | 0.81% | 1.01x | ✅ |
| `pip_freeze` | 0.24242115879999346 | 0.2438931337999975 | -0.61% | -0.60% | 0.99x | ❌ |
| `platform_info` | 3.0323289130331913e-06 | 3.5000130042177833e-06 | -15.42% | -13.36% | 0.87x | ❌ |
| `python_version` | 1.172853035324273e-06 | 1.269092038809386e-06 | -8.21% | -7.58% | 0.92x | ❌ |
