#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.26079598459999714 | 0.2539574182000138 | 2.62% | 2.69% | 1.03x | ✅ |
| `pip_freeze` | 0.2551579095999955 | 0.2555201044000114 | -0.14% | -0.14% | 1.00x | ❌ |
| `platform_info` | 3.1737826689980477e-06 | 3.3260144028550115e-06 | -4.80% | -4.58% | 0.95x | ❌ |
| `python_version` | 1.2200916730557684e-06 | 1.3876135808241656e-06 | -13.73% | -12.07% | 0.88x | ❌ |
