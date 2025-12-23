#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00019344126161342288 | 0.00019605897272060346 | -1.35% | -1.34% | 0.99x | ❌ |
| `get_logger` | 4.516221813440867e-05 | 4.2886129476749474e-05 | 5.04% | 5.31% | 1.05x | ✅ |
| `setup_DEBUG2_logging` | 1.197483001340006e-06 | 1.0594103536424359e-06 | 11.53% | 13.03% | 1.13x | ✅ |
