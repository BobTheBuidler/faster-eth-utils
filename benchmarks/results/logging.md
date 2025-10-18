#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00024419841200081296 | 0.00024408050044652003 | 0.05% | 0.05% | 1.00x | ✅ |
| `get_logger` | 5.068851762557197e-05 | 5.042387560742766e-05 | 0.52% | 0.52% | 1.01x | ✅ |
| `setup_DEBUG2_logging` | 1.080942908167839e-06 | 9.957549968453358e-07 | 7.88% | 8.56% | 1.09x | ✅ |
