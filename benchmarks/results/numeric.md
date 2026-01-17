#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.379930387808185e-05 | 6.488274993238073e-05 | 12.08% | 13.74% | 1.14x | ✅ |
| `clamp[at-lower]` | 7.34189291593907e-05 | 6.621555130024397e-05 | 9.81% | 10.88% | 1.11x | ✅ |
| `clamp[at-upper]` | 7.166459873578533e-05 | 6.397811070391004e-05 | 10.73% | 12.01% | 1.12x | ✅ |
| `clamp[below-lower]` | 6.758751681358192e-05 | 5.683929302993891e-05 | 15.90% | 18.91% | 1.19x | ✅ |
| `clamp[within-bounds]` | 7.245680918003462e-05 | 6.546236028599507e-05 | 9.65% | 10.68% | 1.11x | ✅ |
