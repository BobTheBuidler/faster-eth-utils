#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.193830611182369e-05 | 7.120405668110265e-05 | 1.02% | 1.03% | 1.01x | ✅ |
| `clamp[at-lower]` | 7.005791560660171e-05 | 6.963942362673565e-05 | 0.60% | 0.60% | 1.01x | ✅ |
| `clamp[at-upper]` | 7.098988510191141e-05 | 6.736163643530155e-05 | 5.11% | 5.39% | 1.05x | ✅ |
| `clamp[below-lower]` | 6.52883810997352e-05 | 6.300554680326383e-05 | 3.50% | 3.62% | 1.04x | ✅ |
| `clamp[within-bounds]` | 7.02097028571685e-05 | 7.190322539883476e-05 | -2.41% | -2.36% | 0.98x | ❌ |
