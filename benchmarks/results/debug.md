#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2502206303999969 | 0.2644227691999845 | -5.68% | -5.37% | 0.95x | ❌ |
| `pip_freeze` | 0.2541200853999953 | 0.24855326820000984 | 2.19% | 2.24% | 1.02x | ✅ |
| `platform_info` | 2.887099733449512e-06 | 3.44212345664967e-06 | -19.22% | -16.12% | 0.84x | ❌ |
| `python_version` | 1.1268257177339635e-06 | 1.3154036077092734e-06 | -16.74% | -14.34% | 0.86x | ❌ |
