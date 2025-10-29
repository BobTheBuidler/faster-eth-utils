#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.3133763830000021 | 0.30934375519999546 | 1.29% | 1.30% | 1.01x | ✅ |
| `pip_freeze` | 0.3094191464000119 | 0.3135106112000017 | -1.32% | -1.31% | 0.99x | ❌ |
| `platform_info` | 3.189852303584177e-06 | 3.3140298023978034e-06 | -3.89% | -3.75% | 0.96x | ❌ |
| `python_version` | 1.2274639666398278e-06 | 1.4298404899073274e-06 | -16.49% | -14.15% | 0.86x | ❌ |
