#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021540739736435868 | 0.00021367083795870848 | 0.81% | 0.81% | 1.01x | ✅ |
| `get_logger` | 4.91094322743365e-05 | 4.5566109011775623e-05 | 7.22% | 7.78% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3675791884788268e-06 | 1.287869556760664e-06 | 5.83% | 6.19% | 1.06x | ✅ |
