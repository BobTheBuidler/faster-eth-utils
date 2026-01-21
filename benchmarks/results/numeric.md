#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.111713190324781e-05 | 6.687008822482274e-05 | 5.97% | 6.35% | 1.06x | ✅ |
| `clamp[at-lower]` | 6.970470852489832e-05 | 6.537781614463326e-05 | 6.21% | 6.62% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.185126327526007e-05 | 6.485917994308427e-05 | 9.73% | 10.78% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.347971201993428e-05 | 5.65647960404962e-05 | 10.89% | 12.22% | 1.12x | ✅ |
| `clamp[within-bounds]` | 7.018903263764315e-05 | 6.635643291736981e-05 | 5.46% | 5.78% | 1.06x | ✅ |
