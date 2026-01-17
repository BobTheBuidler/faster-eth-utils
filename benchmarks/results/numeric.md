#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.481677197130263e-05 | 6.650747033769238e-05 | 11.11% | 12.49% | 1.12x | ✅ |
| `clamp[at-lower]` | 7.284628392844674e-05 | 6.630639109377957e-05 | 8.98% | 9.86% | 1.10x | ✅ |
| `clamp[at-upper]` | 7.325582680956269e-05 | 6.86398667519929e-05 | 6.30% | 6.72% | 1.07x | ✅ |
| `clamp[below-lower]` | 6.906412396021795e-05 | 5.707862113709223e-05 | 17.35% | 21.00% | 1.21x | ✅ |
| `clamp[within-bounds]` | 7.270826750657715e-05 | 6.70757567098605e-05 | 7.75% | 8.40% | 1.08x | ✅ |
