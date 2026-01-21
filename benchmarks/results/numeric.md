#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.490085531937455e-05 | 6.656845151253163e-05 | 11.12% | 12.52% | 1.13x | ✅ |
| `clamp[at-lower]` | 7.343947942834429e-05 | 6.872009064340196e-05 | 6.43% | 6.87% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.22406926924962e-05 | 6.657234791058387e-05 | 7.85% | 8.51% | 1.09x | ✅ |
| `clamp[below-lower]` | 6.890798662104278e-05 | 5.711048530682224e-05 | 17.12% | 20.66% | 1.21x | ✅ |
| `clamp[within-bounds]` | 7.05000226804254e-05 | 6.684359782358494e-05 | 5.19% | 5.47% | 1.05x | ✅ |
