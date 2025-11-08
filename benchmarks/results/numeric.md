#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.166322538333388e-05 | 7.005963703865844e-05 | 2.24% | 2.29% | 1.02x | ✅ |
| `clamp[at-lower]` | 7.070294903657451e-05 | 6.62845694704442e-05 | 6.25% | 6.67% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.2197128239764e-05 | 6.649662995434214e-05 | 7.90% | 8.57% | 1.09x | ✅ |
| `clamp[below-lower]` | 6.682395655610018e-05 | 5.910764221733336e-05 | 11.55% | 13.05% | 1.13x | ✅ |
| `clamp[within-bounds]` | 6.99828409924567e-05 | 6.746609089667351e-05 | 3.60% | 3.73% | 1.04x | ✅ |
