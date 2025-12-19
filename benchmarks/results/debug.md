#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23433689299999969 | 0.23570481780000135 | -0.58% | -0.58% | 0.99x | ❌ |
| `pip_freeze` | 0.23428134259997932 | 0.23411708659999703 | 0.07% | 0.07% | 1.00x | ✅ |
| `platform_info` | 3.0566693555919475e-06 | 3.5166843124765505e-06 | -15.05% | -13.08% | 0.87x | ❌ |
| `python_version` | 1.1554705974382739e-06 | 1.2771362987947765e-06 | -10.53% | -9.53% | 0.90x | ❌ |
