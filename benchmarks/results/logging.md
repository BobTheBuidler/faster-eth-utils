#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002144223214287734 | 0.00021765748143428378 | -1.51% | -1.49% | 0.99x | ❌ |
| `get_logger` | 4.933795090135026e-05 | 4.584325338680313e-05 | 7.08% | 7.62% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3006112920200588e-06 | 1.2062590337337363e-06 | 7.25% | 7.82% | 1.08x | ✅ |
