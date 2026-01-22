#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00019347684621055444 | 0.00019404058926061622 | -0.29% | -0.29% | 1.00x | ❌ |
| `get_logger` | 4.50019610128202e-05 | 4.210823301162412e-05 | 6.43% | 6.87% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.1615850939053826e-06 | 1.0575630817449945e-06 | 8.96% | 9.84% | 1.10x | ✅ |
