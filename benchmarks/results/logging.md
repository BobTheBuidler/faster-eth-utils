#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002166747677442781 | 0.00021884728176643157 | -1.00% | -0.99% | 0.99x | ❌ |
| `get_logger` | 4.82219620999115e-05 | 4.207172856283766e-05 | 12.75% | 14.62% | 1.15x | ✅ |
| `setup_DEBUG2_logging` | 1.3562456200388595e-06 | 1.2461921334271744e-06 | 8.11% | 8.83% | 1.09x | ✅ |
