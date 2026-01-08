#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021389977047421457 | 0.00021123239492156442 | 1.25% | 1.26% | 1.01x | ✅ |
| `get_logger` | 4.7694061741574446e-05 | 4.441087553571123e-05 | 6.88% | 7.39% | 1.07x | ✅ |
| `setup_DEBUG2_logging` | 1.340103067748501e-06 | 1.2663390444538214e-06 | 5.50% | 5.82% | 1.06x | ✅ |
