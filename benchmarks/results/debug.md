#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2820934082000008 | 0.28026813300000414 | 0.65% | 0.65% | 1.01x | ✅ |
| `pip_freeze` | 0.27054094880001 | 0.2713792741999896 | -0.31% | -0.31% | 1.00x | ❌ |
| `platform_info` | 2.9055566711939585e-06 | 3.3913719338727522e-06 | -16.72% | -14.33% | 0.86x | ❌ |
| `python_version` | 1.0861650925289739e-06 | 1.3178073746447337e-06 | -21.33% | -17.58% | 0.82x | ❌ |
