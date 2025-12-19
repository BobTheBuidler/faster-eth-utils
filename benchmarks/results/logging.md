#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00019450322134258836 | 0.00019654585837936334 | -1.05% | -1.04% | 0.99x | ❌ |
| `get_logger` | 4.529308389090078e-05 | 4.339994796286922e-05 | 4.18% | 4.36% | 1.04x | ✅ |
| `setup_DEBUG2_logging` | 1.1961916639405261e-06 | 1.0864206249533412e-06 | 9.18% | 10.10% | 1.10x | ✅ |
