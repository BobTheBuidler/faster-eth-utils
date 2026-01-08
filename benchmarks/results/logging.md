#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002095337675566844 | 0.00020805555949606389 | 0.71% | 0.71% | 1.01x | ✅ |
| `get_logger` | 4.80893486209903e-05 | 4.4578500821256495e-05 | 7.30% | 7.88% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3681635052713626e-06 | 1.284650767579244e-06 | 6.10% | 6.50% | 1.07x | ✅ |
