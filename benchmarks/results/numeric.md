#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.764725938239627e-05 | 7.748455270731257e-05 | 0.21% | 0.21% | 1.00x | ✅ |
| `clamp[at-lower]` | 7.504869070704313e-05 | 7.62819302963207e-05 | -1.64% | -1.62% | 0.98x | ❌ |
| `clamp[at-upper]` | 7.39718223143049e-05 | 7.764247873629759e-05 | -4.96% | -4.73% | 0.95x | ❌ |
| `clamp[below-lower]` | 6.76695532196846e-05 | 6.691857540637703e-05 | 1.11% | 1.12% | 1.01x | ✅ |
| `clamp[within-bounds]` | 7.647673445003123e-05 | 7.762764502142335e-05 | -1.50% | -1.48% | 0.99x | ❌ |
