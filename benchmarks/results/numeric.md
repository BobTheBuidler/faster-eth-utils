#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.040286089859e-05 | 7.256960950190339e-05 | -3.08% | -2.99% | 0.97x | ❌ |
| `clamp[at-lower]` | 7.05758185119693e-05 | 6.867220451007619e-05 | 2.70% | 2.77% | 1.03x | ✅ |
| `clamp[at-upper]` | 6.525907993203887e-05 | 7.401621816988711e-05 | -13.42% | -11.83% | 0.88x | ❌ |
| `clamp[below-lower]` | 6.239317916665602e-05 | 6.291438511949268e-05 | -0.84% | -0.83% | 0.99x | ❌ |
| `clamp[within-bounds]` | 7.070656944953059e-05 | 6.934330929598809e-05 | 1.93% | 1.97% | 1.02x | ✅ |
