#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23568106239999906 | 0.23330792020001354 | 1.01% | 1.02% | 1.01x | ✅ |
| `pip_freeze` | 0.2360932526000056 | 0.235575040599997 | 0.22% | 0.22% | 1.00x | ✅ |
| `platform_info` | 3.070853946652326e-06 | 3.6417531649230935e-06 | -18.59% | -15.68% | 0.84x | ❌ |
| `python_version` | 1.1861927362398404e-06 | 1.375406498603887e-06 | -15.95% | -13.76% | 0.86x | ❌ |
