#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.052692457896776e-05 | 7.330251260862685e-05 | -3.94% | -3.79% | 0.96x | ❌ |
| `clamp[at-lower]` | 7.125528529784432e-05 | 7.270186643205189e-05 | -2.03% | -1.99% | 0.98x | ❌ |
| `clamp[at-upper]` | 7.041704197367902e-05 | 7.176154843204184e-05 | -1.91% | -1.87% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.617649210247033e-05 | 6.316975516790792e-05 | 4.54% | 4.76% | 1.05x | ✅ |
| `clamp[within-bounds]` | 7.066503608259382e-05 | 7.441536395211981e-05 | -5.31% | -5.04% | 0.95x | ❌ |
