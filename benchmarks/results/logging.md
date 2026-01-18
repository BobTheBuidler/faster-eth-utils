#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021279259596626742 | 0.0002073991967674498 | 2.53% | 2.60% | 1.03x | ✅ |
| `get_logger` | 4.8803491422076175e-05 | 4.4605230246687876e-05 | 8.60% | 9.41% | 1.09x | ✅ |
| `setup_DEBUG2_logging` | 1.3648875715984326e-06 | 1.281468447407541e-06 | 6.11% | 6.51% | 1.07x | ✅ |
