#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2235791200000108 | 0.21970978319999404 | 1.73% | 1.76% | 1.02x | ✅ |
| `pip_freeze` | 0.2254899249999994 | 0.22419966939999086 | 0.57% | 0.58% | 1.01x | ✅ |
| `platform_info` | 2.9132350177310244e-06 | 3.1503878604591558e-06 | -8.14% | -7.53% | 0.92x | ❌ |
| `python_version` | 1.158574717282258e-06 | 1.141057361208889e-06 | 1.51% | 1.54% | 1.02x | ✅ |
