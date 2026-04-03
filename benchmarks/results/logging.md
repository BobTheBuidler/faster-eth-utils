#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021019810609868017 | 0.00020664969529101207 | 1.69% | 1.72% | 1.02x | ✅ |
| `get_logger` | 4.8569766800298525e-05 | 4.560223386161729e-05 | 6.11% | 6.51% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.289179443812147e-06 | 1.2041890394459868e-06 | 6.59% | 7.06% | 1.07x | ✅ |
