#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.0002116171334982341 | 0.00021558720414514252 | -1.88% | -1.84% | 0.98x | ❌ |
| `get_logger` | 4.717237794979245e-05 | 4.622297401669485e-05 | 2.01% | 2.05% | 1.02x | ✅ |
| `setup_DEBUG2_logging` | 1.3061780506840482e-06 | 1.2153925741484662e-06 | 6.95% | 7.47% | 1.07x | ✅ |
