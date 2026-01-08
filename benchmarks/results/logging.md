#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021519718415159112 | 0.00021514118343700118 | 0.03% | 0.03% | 1.00x | ✅ |
| `get_logger` | 4.816964282317428e-05 | 4.47110777372761e-05 | 7.18% | 7.74% | 1.08x | ✅ |
| `setup_DEBUG2_logging` | 1.3493899633236543e-06 | 1.2606817344347141e-06 | 6.57% | 7.04% | 1.07x | ✅ |
