#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021606100077589677 | 0.00021844252112237453 | -1.10% | -1.09% | 0.99x | ❌ |
| `get_logger` | 4.8604756606673713e-05 | 4.610348237186979e-05 | 5.15% | 5.43% | 1.05x | ✅ |
| `setup_DEBUG2_logging` | 1.3378363061220995e-06 | 1.262619210659492e-06 | 5.62% | 5.96% | 1.06x | ✅ |
