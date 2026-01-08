#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021805314278563255 | 0.00021192786783817252 | 2.81% | 2.89% | 1.03x | ✅ |
| `get_logger` | 4.773323421902788e-05 | 4.396213646007345e-05 | 7.90% | 8.58% | 1.09x | ✅ |
| `setup_DEBUG2_logging` | 1.3295076497706615e-06 | 1.2621718214407135e-06 | 5.06% | 5.33% | 1.05x | ✅ |
