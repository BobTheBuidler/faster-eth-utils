#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24659371760000112 | 0.24737562080000544 | -0.32% | -0.32% | 1.00x | ❌ |
| `pip_freeze` | 0.2471305141999892 | 0.24635792059998493 | 0.31% | 0.31% | 1.00x | ✅ |
| `platform_info` | 3.0895554129163373e-06 | 3.1998609076658257e-06 | -3.57% | -3.45% | 0.97x | ❌ |
| `python_version` | 1.1294200632942406e-06 | 1.332445454992743e-06 | -17.98% | -15.24% | 0.85x | ❌ |
