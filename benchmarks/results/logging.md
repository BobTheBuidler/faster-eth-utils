#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00016841324959190947 | 0.00016926731644216323 | -0.51% | -0.50% | 0.99x | ❌ |
| `get_logger` | 3.970636028063027e-05 | 3.709499427226098e-05 | 6.58% | 7.04% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.0184294973003253e-06 | 9.117358756478376e-07 | 10.48% | 11.70% | 1.12x | ✅ |
