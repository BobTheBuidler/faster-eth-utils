#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.445387599085359e-05 | 7.084635229403549e-05 | -30.10% | -23.14% | 0.77x | ❌ |
| `clamp[at-lower]` | 5.4061624214487346e-05 | 7.145091647856353e-05 | -32.17% | -24.34% | 0.76x | ❌ |
| `clamp[at-upper]` | 5.3937537784371365e-05 | 7.158593723043836e-05 | -32.72% | -24.65% | 0.75x | ❌ |
| `clamp[below-lower]` | 4.9818452161984676e-05 | 6.082207291273894e-05 | -22.09% | -18.09% | 0.82x | ❌ |
| `clamp[within-bounds]` | 5.420811218564539e-05 | 7.202908540079035e-05 | -32.88% | -24.74% | 0.75x | ❌ |
