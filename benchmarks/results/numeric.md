#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.797459121903575e-05 | 7.485600271920544e-05 | -10.12% | -9.19% | 0.91x | ❌ |
| `clamp[at-lower]` | 6.64183608191306e-05 | 7.054599711980104e-05 | -6.21% | -5.85% | 0.94x | ❌ |
| `clamp[at-upper]` | 6.831922759604542e-05 | 7.29845237038339e-05 | -6.83% | -6.39% | 0.94x | ❌ |
| `clamp[below-lower]` | 6.45986444272612e-05 | 6.366907206831772e-05 | 1.44% | 1.46% | 1.01x | ✅ |
| `clamp[within-bounds]` | 6.708587719186695e-05 | 7.434154142014597e-05 | -10.82% | -9.76% | 0.90x | ❌ |
