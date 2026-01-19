#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2384919353999976 | 0.23699261339999111 | 0.63% | 0.63% | 1.01x | ✅ |
| `pip_freeze` | 0.2384745280000061 | 0.2379828763999967 | 0.21% | 0.21% | 1.00x | ✅ |
| `platform_info` | 3.0439921878677723e-06 | 3.6833915953040013e-06 | -21.01% | -17.36% | 0.83x | ❌ |
| `python_version` | 1.1650212007514365e-06 | 1.399922762387936e-06 | -20.16% | -16.78% | 0.83x | ❌ |
