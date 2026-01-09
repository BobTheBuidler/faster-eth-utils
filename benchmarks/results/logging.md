#### [faster_eth_utils.logging](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/logging.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_logging_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `get_extended_debug_logger` | 0.00021505479296927513 | 0.00021243038628642998 | 1.22% | 1.24% | 1.01x | ✅ |
| `get_logger` | 4.9336328372372984e-05 | 4.488891009357928e-05 | 9.01% | 9.91% | 1.10x | ✅ |
| `setup_DEBUG2_logging` | 1.391395850368512e-06 | 1.307457902111519e-06 | 6.03% | 6.42% | 1.06x | ✅ |
