#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.011046690390764e-05 | 7.365028196082027e-05 | -5.05% | -4.81% | 0.95x | ❌ |
| `clamp[at-lower]` | 7.011259822918778e-05 | 7.390545929090474e-05 | -5.41% | -5.13% | 0.95x | ❌ |
| `clamp[at-upper]` | 6.937695938867287e-05 | 7.517875408665356e-05 | -8.36% | -7.72% | 0.92x | ❌ |
| `clamp[below-lower]` | 6.299528180462253e-05 | 6.337294559618226e-05 | -0.60% | -0.60% | 0.99x | ❌ |
| `clamp[within-bounds]` | 7.085141045913835e-05 | 7.243245559994023e-05 | -2.23% | -2.18% | 0.98x | ❌ |
