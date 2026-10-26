#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021818034376960385 | 0.0002193204981041977 | -0.52% | -0.52% | 0.99x | ❌ |
| `get_logger` | 5.103392240159925e-05 | 4.871030229470953e-05 | 4.55% | 4.77% | 1.05x | ✅ |
| `setup_DEBUG2_logging` | 1.2304174889593e-06 | 1.1414325286489243e-06 | 7.23% | 7.80% | 1.08x | ✅ |
