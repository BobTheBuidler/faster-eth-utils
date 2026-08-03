#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2549127927999848 | 0.245045692400015 | 3.87% | 4.03% | 1.04x | ✅ |
| `pip_freeze` | 0.250208698400013 | 0.25093645739999604 | -0.29% | -0.29% | 1.00x | ❌ |
| `platform_info` | 3.226890676101622e-06 | 3.2556738871990644e-06 | -0.89% | -0.88% | 0.99x | ❌ |
| `python_version` | 1.1596125268901077e-06 | 1.3421484527707323e-06 | -15.74% | -13.60% | 0.86x | ❌ |
