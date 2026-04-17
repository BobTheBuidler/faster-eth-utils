#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.701333146402847e-05 | 7.275905107438848e-05 | -8.57% | -7.90% | 0.92x | ❌ |
| `clamp[at-lower]` | 6.925002505124659e-05 | 6.892554998966016e-05 | 0.47% | 0.47% | 1.00x | ✅ |
| `clamp[at-upper]` | 7.043028304187305e-05 | 7.021782490751118e-05 | 0.30% | 0.30% | 1.00x | ✅ |
| `clamp[below-lower]` | 6.056465848850833e-05 | 6.342322239470566e-05 | -4.72% | -4.51% | 0.95x | ❌ |
| `clamp[within-bounds]` | 7.007748876811544e-05 | 7.1364968791614e-05 | -1.84% | -1.80% | 0.98x | ❌ |
