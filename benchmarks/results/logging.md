#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021418431339325898 | 0.00021280743771308612 | 0.64% | 0.65% | 1.01x | ✅ |
| `get_logger` | 4.768212105285652e-05 | 4.5110844117454415e-05 | 5.39% | 5.70% | 1.06x | ✅ |
| `setup_DEBUG2_logging` | 1.2871560508256015e-06 | 1.2030545048968322e-06 | 6.53% | 6.99% | 1.07x | ✅ |
