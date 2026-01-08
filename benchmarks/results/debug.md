#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23954519000001256 | 0.24063287660000016 | -0.45% | -0.45% | 1.00x | ❌ |
| `pip_freeze` | 0.241525973399996 | 0.2408459784000229 | 0.28% | 0.28% | 1.00x | ✅ |
| `platform_info` | 3.0938474819789246e-06 | 3.392690128851177e-06 | -9.66% | -8.81% | 0.91x | ❌ |
| `python_version` | 1.1644989153957222e-06 | 1.1647050822172147e-06 | -0.02% | -0.02% | 1.00x | ❌ |
