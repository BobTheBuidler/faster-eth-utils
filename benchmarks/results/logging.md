#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002130767699504695 | 0.0002109183407045052 | 1.01% | 1.02% | 1.01x | ✅ |
| `get_logger` | 4.8889727644102096e-05 | 4.452002473121281e-05 | 8.94% | 9.82% | 1.10x | ✅ |
| `setup_DEBUG2_logging` | 1.362927304796216e-06 | 1.2682738490789118e-06 | 6.94% | 7.46% | 1.07x | ✅ |
