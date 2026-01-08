#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23749432960000832 | 0.23665147140000045 | 0.35% | 0.36% | 1.00x | ✅ |
| `pip_freeze` | 0.2349458047999974 | 0.23612739819999434 | -0.50% | -0.50% | 0.99x | ❌ |
| `platform_info` | 3.1088962386630956e-06 | 3.6339414409822465e-06 | -16.89% | -14.45% | 0.86x | ❌ |
| `python_version` | 1.1865941420619398e-06 | 1.3063798936816044e-06 | -10.09% | -9.17% | 0.91x | ❌ |
