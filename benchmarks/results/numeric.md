#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.479371794614312e-05 | 6.865145170032188e-05 | 8.21% | 8.95% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.478461064472497e-05 | 6.649103394138314e-05 | 11.09% | 12.47% | 1.12x | ✅ |
| `clamp[at-upper]` | 7.574972783519524e-05 | 6.745865799506848e-05 | 10.95% | 12.29% | 1.12x | ✅ |
| `clamp[below-lower]` | 6.884139807728664e-05 | 6.059544888811544e-05 | 11.98% | 13.61% | 1.14x | ✅ |
| `clamp[within-bounds]` | 7.436209896326479e-05 | 6.915162753780186e-05 | 7.01% | 7.53% | 1.08x | ✅ |
