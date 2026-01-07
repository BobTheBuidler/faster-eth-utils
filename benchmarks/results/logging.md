#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021557683552628294 | 0.00021058104620224791 | 2.32% | 2.37% | 1.02x | ✅ |
| `get_logger` | 4.970242646561608e-05 | 4.440838606525063e-05 | 10.65% | 11.92% | 1.12x | ✅ |
| `setup_DEBUG2_logging` | 1.3588651912359538e-06 | 1.2614869111012403e-06 | 7.17% | 7.72% | 1.08x | ✅ |
