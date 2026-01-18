#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002101266500665058 | 0.0002086225223273732 | 0.72% | 0.72% | 1.01x | ✅ |
| `get_logger` | 4.8991949179242494e-05 | 4.598684959171779e-05 | 6.13% | 6.53% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.3498176268927636e-06 | 1.2614627461925512e-06 | 6.55% | 7.00% | 1.07x | ✅ |
