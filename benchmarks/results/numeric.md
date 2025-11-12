#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.566824912884592e-05 | 7.146013330801286e-05 | 5.56% | 5.89% | 1.06x | ✅ |
| `clamp[at-lower]` | 7.532263384373175e-05 | 6.962995654056218e-05 | 7.56% | 8.18% | 1.08x | ✅ |
| `clamp[at-upper]` | 7.471239004969167e-05 | 7.021348202200799e-05 | 6.02% | 6.41% | 1.06x | ✅ |
| `clamp[below-lower]` | 6.954537722098382e-05 | 6.773067850083183e-05 | 2.61% | 2.68% | 1.03x | ✅ |
| `clamp[within-bounds]` | 7.402397545691256e-05 | 7.029955060131347e-05 | 5.03% | 5.30% | 1.05x | ✅ |
