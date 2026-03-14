#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021586117243201251 | 0.00021754164002176947 | -0.78% | -0.77% | 0.99x | ❌ |
| `get_logger` | 5.067106148024571e-05 | 4.5253699654364496e-05 | 10.69% | 11.97% | 1.12x | ✅ |
| `setup_DEBUG2_logging` | 1.2818287832665264e-06 | 1.1714982547729247e-06 | 8.61% | 9.42% | 1.09x | ✅ |
