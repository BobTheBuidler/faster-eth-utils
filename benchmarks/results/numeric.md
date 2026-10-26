#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.852151742585988e-05 | 7.052667077358546e-05 | -2.93% | -2.84% | 0.97x | ❌ |
| `clamp[at-lower]` | 6.907464189537925e-05 | 6.844324180815246e-05 | 0.91% | 0.92% | 1.01x | ✅ |
| `clamp[at-upper]` | 6.79022692649078e-05 | 6.926093273705527e-05 | -2.00% | -1.96% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.122517993520246e-05 | 6.13773032261586e-05 | -0.25% | -0.25% | 1.00x | ❌ |
| `clamp[within-bounds]` | 6.963870074898366e-05 | 7.069711673952837e-05 | -1.52% | -1.50% | 0.99x | ❌ |
