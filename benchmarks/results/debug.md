#### [faster_eth_utils.debug](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/debug.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_debug_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_environment_summary` | 0.23430771679999224 | 0.23513433860000532 | -0.35% | -0.35% | 1.00x | ❌ |
| `pip_freeze` | 0.23737941580001234 | 0.2451636981999968 | -3.28% | -3.18% | 0.97x | ❌ |
| `platform_info` | 3.116711312792314e-06 | 3.684324343039888e-06 | -18.21% | -15.41% | 0.85x | ❌ |
| `python_version` | 1.2060019075091572e-06 | 1.2862362856621e-06 | -6.65% | -6.24% | 0.94x | ❌ |
