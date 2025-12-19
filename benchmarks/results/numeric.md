#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.566292976474319e-05 | 6.721991673076027e-05 | 11.16% | 12.56% | 1.13x | ✅ |
| `clamp[at-lower]` | 7.347759623200229e-05 | 6.592737554774536e-05 | 10.28% | 11.45% | 1.11x | ✅ |
| `clamp[at-upper]` | 7.469511840106592e-05 | 6.714137126660936e-05 | 10.11% | 11.25% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.736200224729931e-05 | 5.966232120113966e-05 | 11.43% | 12.91% | 1.13x | ✅ |
| `clamp[within-bounds]` | 7.382622174916294e-05 | 6.865581223752649e-05 | 7.00% | 7.53% | 1.08x | ✅ |
