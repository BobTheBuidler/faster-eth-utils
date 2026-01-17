#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.2334492302000058 | 0.23844973660001187 | -2.14% | -2.10% | 0.98x | ❌ |
| `pip_freeze` | 0.2334876427999916 | 0.23347571120001476 | 0.01% | 0.01% | 1.00x | ✅ |
| `platform_info` | 3.113342779486239e-06 | 3.6084305498419285e-06 | -15.90% | -13.72% | 0.86x | ❌ |
| `python_version` | 1.1744752059674468e-06 | 1.2601580956987187e-06 | -7.30% | -6.80% | 0.93x | ❌ |
