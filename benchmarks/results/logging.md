#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021653399869320434 | 0.00021235922458121912 | 1.93% | 1.97% | 1.02x | ✅ |
| `get_logger` | 4.931734248509708e-05 | 4.475463996345864e-05 | 9.25% | 10.19% | 1.10x | ✅ |
| `setup_DEBUG2_logging` | 1.339283830728802e-06 | 1.2472260267651656e-06 | 6.87% | 7.38% | 1.07x | ✅ |
