#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002223934517501346 | 0.00021713849811972843 | 2.36% | 2.42% | 1.02x | ✅ |
| `get_logger` | 5.1618688134815385e-05 | 4.84218990967371e-05 | 6.19% | 6.60% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.363447540516089e-06 | 1.2790016479385096e-06 | 6.19% | 6.60% | 1.07x | ✅ |
