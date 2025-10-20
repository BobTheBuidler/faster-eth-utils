#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.818698649177717e-05 | 7.817280349077672e-05 | -14.64% | -12.77% | 0.87x | ❌ |
| `clamp[at-lower]` | 6.70376812367545e-05 | 7.53621122588934e-05 | -12.42% | -11.05% | 0.89x | ❌ |
| `clamp[at-upper]` | 6.689653034235673e-05 | 7.54344884044541e-05 | -12.76% | -11.32% | 0.89x | ❌ |
| `clamp[below-lower]` | 6.37289978824246e-05 | 6.586749759792349e-05 | -3.36% | -3.25% | 0.97x | ❌ |
| `clamp[within-bounds]` | 6.657625610520937e-05 | 7.426945438908445e-05 | -11.56% | -10.36% | 0.90x | ❌ |
