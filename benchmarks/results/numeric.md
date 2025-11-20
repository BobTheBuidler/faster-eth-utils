#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.7848449241899085e-05 | 6.270776528144137e-05 | -8.40% | -7.75% | 0.92x | ❌ |
| `clamp[at-lower]` | 5.7725421870921925e-05 | 6.283795158286773e-05 | -8.86% | -8.14% | 0.92x | ❌ |
| `clamp[at-upper]` | 5.726741502676818e-05 | 6.230271077829648e-05 | -8.79% | -8.08% | 0.92x | ❌ |
| `clamp[below-lower]` | 5.162471141364204e-05 | 5.543861303115347e-05 | -7.39% | -6.88% | 0.93x | ❌ |
| `clamp[within-bounds]` | 5.748817591416976e-05 | 6.323708666148015e-05 | -10.00% | -9.09% | 0.91x | ❌ |
