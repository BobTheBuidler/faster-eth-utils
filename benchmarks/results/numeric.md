#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.345863549359766e-05 | 6.498536671735744e-05 | 11.53% | 13.04% | 1.13x | ✅ |
| `clamp[at-lower]` | 7.35278260839826e-05 | 6.518059042860421e-05 | 11.35% | 12.81% | 1.13x | ✅ |
| `clamp[at-upper]` | 7.260483586485891e-05 | 6.481657109662234e-05 | 10.73% | 12.02% | 1.12x | ✅ |
| `clamp[below-lower]` | 6.829136614854187e-05 | 5.8251158884624995e-05 | 14.70% | 17.24% | 1.17x | ✅ |
| `clamp[within-bounds]` | 7.269148301714053e-05 | 6.551002596632246e-05 | 9.88% | 10.96% | 1.11x | ✅ |
