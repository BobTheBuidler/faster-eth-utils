#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021484933675556625 | 0.0002129082419195218 | 0.90% | 0.91% | 1.01x | ✅ |
| `get_logger` | 4.793547475966598e-05 | 4.430129121963857e-05 | 7.58% | 8.20% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3630215136326738e-06 | 1.284172527522177e-06 | 5.78% | 6.14% | 1.06x | ✅ |
