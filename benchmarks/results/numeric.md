#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.073783229553292e-05 | 7.041875368337515e-05 | 0.45% | 0.45% | 1.00x | ✅ |
| `clamp[at-lower]` | 7.148581216408243e-05 | 7.061118356720731e-05 | 1.22% | 1.24% | 1.01x | ✅ |
| `clamp[at-upper]` | 6.961032111336233e-05 | 7.081226217181247e-05 | -1.73% | -1.70% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.524292733194856e-05 | 6.132482979607437e-05 | 6.01% | 6.39% | 1.06x | ✅ |
| `clamp[within-bounds]` | 7.265050186896173e-05 | 7.080290421477339e-05 | 2.54% | 2.61% | 1.03x | ✅ |
