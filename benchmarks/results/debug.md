#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.3007690274000424 | 0.3007030964000023 | 0.02% | 0.02% | 1.00x | ✅ |
| `pip_freeze` | 0.2996558288000074 | 0.30008474019999765 | -0.14% | -0.14% | 1.00x | ❌ |
| `platform_info` | 3.174795784551728e-06 | 3.3302301590886917e-06 | -4.90% | -4.67% | 0.95x | ❌ |
| `python_version` | 1.2482999061808744e-06 | 1.3388713343274028e-06 | -7.26% | -6.76% | 0.93x | ❌ |
