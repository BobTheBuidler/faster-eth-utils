#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021758410640817656 | 0.00021145565201159946 | 2.82% | 2.90% | 1.03x | ✅ |
| `get_logger` | 4.8035665547196866e-05 | 4.804584997600831e-05 | -0.02% | -0.02% | 1.00x | ❌ |
| `setup_DEBUG2_logging` | 1.3854405969022711e-06 | 1.2717216618279988e-06 | 8.21% | 8.94% | 1.09x | ✅ |
