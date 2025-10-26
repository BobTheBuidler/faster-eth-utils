#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002179842064893746 | 0.00021718794679751832 | 0.37% | 0.37% | 1.00x | ✅ |
| `get_logger` | 4.78450394803468e-05 | 4.851225559305009e-05 | -1.39% | -1.38% | 0.99x | ❌ |
| `setup_DEBUG2_logging` | 1.3006188033435252e-06 | 1.2100023322804476e-06 | 6.97% | 7.49% | 1.07x | ✅ |
