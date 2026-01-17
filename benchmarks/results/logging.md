#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021628627048340528 | 0.0002127098465859806 | 1.65% | 1.68% | 1.02x | ✅ |
| `get_logger` | 4.953305957097376e-05 | 4.454535852270553e-05 | 10.07% | 11.20% | 1.11x | ✅ |
| `setup_DEBUG2_logging` | 1.3276335414471523e-06 | 1.2568864984759346e-06 | 5.33% | 5.63% | 1.06x | ✅ |
