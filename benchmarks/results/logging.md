#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021446321582921292 | 0.00021210487183763191 | 1.10% | 1.11% | 1.01x | ✅ |
| `get_logger` | 4.796731306881184e-05 | 4.42545607829271e-05 | 7.74% | 8.39% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3818009784158942e-06 | 1.2680922286520292e-06 | 8.23% | 8.97% | 1.09x | ✅ |
