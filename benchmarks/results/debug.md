#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.26115145620000246 | 0.259171740599993 | 0.76% | 0.76% | 1.01x | ✅ |
| `pip_freeze` | 0.2572130614000116 | 0.2597036410000214 | -0.97% | -0.96% | 0.99x | ❌ |
| `platform_info` | 2.687875530457382e-06 | 2.9096648238202233e-06 | -8.25% | -7.62% | 0.92x | ❌ |
| `python_version` | 1.077321341596482e-06 | 1.278655760240482e-06 | -18.69% | -15.75% | 0.84x | ❌ |
