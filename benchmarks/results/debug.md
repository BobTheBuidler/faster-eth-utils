#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23791306959999475 | 0.23791239899999256 | 0.00% | 0.00% | 1.00x | ✅ |
| `pip_freeze` | 0.2373502500000086 | 0.2352459682000017 | 0.89% | 0.89% | 1.01x | ✅ |
| `platform_info` | 3.1466893334860894e-06 | 3.7100177845580145e-06 | -17.90% | -15.18% | 0.85x | ❌ |
| `python_version` | 1.4332567173034158e-06 | 1.31937886647497e-06 | 7.95% | 8.63% | 1.09x | ✅ |
