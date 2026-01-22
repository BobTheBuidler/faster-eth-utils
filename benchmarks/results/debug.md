#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.22635491539999747 | 0.2259106087999953 | 0.20% | 0.20% | 1.00x | ✅ |
| `pip_freeze` | 0.21733815760001107 | 0.2172905679999758 | 0.02% | 0.02% | 1.00x | ✅ |
| `platform_info` | 2.8515565116741263e-06 | 3.0178575616035237e-06 | -5.83% | -5.51% | 0.94x | ❌ |
| `python_version` | 1.1638222485577693e-06 | 1.1462158820017107e-06 | 1.51% | 1.54% | 1.02x | ✅ |
