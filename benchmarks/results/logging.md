#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021211463890316714 | 0.00021647179100268355 | -2.05% | -2.01% | 0.98x | ❌ |
| `get_logger` | 4.737285930385743e-05 | 4.420468323679309e-05 | 6.69% | 7.17% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.3331201265337035e-06 | 1.2665935921289975e-06 | 4.99% | 5.25% | 1.05x | ✅ |
