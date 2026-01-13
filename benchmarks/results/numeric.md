#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.427283553679155e-05 | 6.743916862872702e-05 | 9.20% | 10.13% | 1.10x | ✅ |
| `clamp[at-lower]` | 7.337689182562674e-05 | 6.75608568295277e-05 | 7.93% | 8.61% | 1.09x | ✅ |
| `clamp[at-upper]` | 7.338322280635294e-05 | 6.631150739605662e-05 | 9.64% | 10.66% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.851281487520218e-05 | 6.116579344465609e-05 | 10.72% | 12.01% | 1.12x | ✅ |
| `clamp[within-bounds]` | 7.332630561054322e-05 | 6.819514446067155e-05 | 7.00% | 7.52% | 1.08x | ✅ |
