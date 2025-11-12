#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021540341958037942 | 0.0002190254577283077 | -1.68% | -1.65% | 0.98x | ❌ |
| `get_logger` | 4.875640271213325e-05 | 4.584891327983044e-05 | 5.96% | 6.34% | 1.06x | ✅ |
| `setup_DEBUG2_logging` | 1.411179289953052e-06 | 1.3215565701255862e-06 | 6.35% | 6.78% | 1.07x | ✅ |
