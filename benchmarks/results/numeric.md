#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.150389939117315e-05 | 7.479602198197525e-05 | -4.60% | -4.40% | 0.96x | ❌ |
| `clamp[at-lower]` | 6.895372258664311e-05 | 7.241769429540105e-05 | -5.02% | -4.78% | 0.95x | ❌ |
| `clamp[at-upper]` | 6.974075676804419e-05 | 7.152874035755056e-05 | -2.56% | -2.50% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.478245267577844e-05 | 6.533419573323037e-05 | -0.85% | -0.84% | 0.99x | ❌ |
| `clamp[within-bounds]` | 7.008885948559122e-05 | 7.444994718055368e-05 | -6.22% | -5.86% | 0.94x | ❌ |
