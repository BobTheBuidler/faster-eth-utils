#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.24404170380001916 | 0.24553038520001563 | -0.61% | -0.61% | 0.99x | ❌ |
| `pip_freeze` | 0.24510806519999734 | 0.24264017059999787 | 1.01% | 1.02% | 1.01x | ✅ |
| `platform_info` | 3.151178423365056e-06 | 3.6084249889763584e-06 | -14.51% | -12.67% | 0.87x | ❌ |
| `python_version` | 1.1773313938572242e-06 | 1.3774727445126215e-06 | -17.00% | -14.53% | 0.85x | ❌ |
