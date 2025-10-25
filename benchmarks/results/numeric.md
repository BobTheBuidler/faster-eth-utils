#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.053582217321463e-05 | 7.249714581792832e-05 | -2.78% | -2.71% | 0.97x | ❌ |
| `clamp[at-lower]` | 7.076842441522727e-05 | 7.110010611473788e-05 | -0.47% | -0.47% | 1.00x | ❌ |
| `clamp[at-upper]` | 7.066661984838684e-05 | 7.132999566747949e-05 | -0.94% | -0.93% | 0.99x | ❌ |
| `clamp[below-lower]` | 6.0566766332202125e-05 | 5.9211953635547794e-05 | 2.24% | 2.29% | 1.02x | ✅ |
| `clamp[within-bounds]` | 6.510206431544032e-05 | 7.357769692152257e-05 | -13.02% | -11.52% | 0.88x | ❌ |
