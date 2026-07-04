#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.648716252675006e-05 | 6.911846589353187e-05 | -3.96% | -3.81% | 0.96x | ❌ |
| `clamp[at-lower]` | 6.573526413248863e-05 | 7.11649245651947e-05 | -8.26% | -7.63% | 0.92x | ❌ |
| `clamp[at-upper]` | 6.735081091332974e-05 | 6.86066735132783e-05 | -1.86% | -1.83% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.14228135219348e-05 | 6.176587292574963e-05 | -0.56% | -0.56% | 0.99x | ❌ |
| `clamp[within-bounds]` | 6.83053354237424e-05 | 6.952417639444825e-05 | -1.78% | -1.75% | 0.98x | ❌ |
