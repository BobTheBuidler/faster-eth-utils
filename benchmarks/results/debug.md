#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.32176703459998635 | 0.32852515820000006 | -2.10% | -2.06% | 0.98x | ❌ |
| `pip_freeze` | 0.32542303319999066 | 0.3225386159999971 | 0.89% | 0.89% | 1.01x | ✅ |
| `platform_info` | 2.8057520211867164e-06 | 3.2939671406234183e-06 | -17.40% | -14.82% | 0.85x | ❌ |
| `python_version` | 1.0637656961265878e-06 | 1.2722932658481727e-06 | -19.60% | -16.39% | 0.84x | ❌ |
