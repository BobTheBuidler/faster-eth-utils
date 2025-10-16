#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021741334541450444 | 0.00021836251624113206 | -0.44% | -0.43% | 1.00x | ❌ |
| `get_logger` | 4.748810665565822e-05 | 4.8011165421921134e-05 | -1.10% | -1.09% | 0.99x | ❌ |
| `setup_DEBUG2_logging` | 1.3270647187996066e-06 | 1.2089111623199464e-06 | 8.90% | 9.77% | 1.10x | ✅ |
