#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00022106861109507005 | 0.00022002241624995215 | 0.47% | 0.48% | 1.00x | ✅ |
| `get_logger` | 5.0180338598515244e-05 | 4.735044379064738e-05 | 5.64% | 5.98% | 1.06x | ✅ |
| `setup_DEBUG2_logging` | 1.2768362291358823e-06 | 1.1397746628360354e-06 | 10.73% | 12.03% | 1.12x | ✅ |
