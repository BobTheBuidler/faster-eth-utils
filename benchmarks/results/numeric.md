#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.056663951312475e-05 | 7.196926537901268e-05 | -1.99% | -1.95% | 0.98x | ❌ |
| `clamp[at-lower]` | 6.869702732906938e-05 | 6.985258126121006e-05 | -1.68% | -1.65% | 0.98x | ❌ |
| `clamp[at-upper]` | 7.051576517415597e-05 | 7.139093731098589e-05 | -1.24% | -1.23% | 0.99x | ❌ |
| `clamp[below-lower]` | 6.383475226470876e-05 | 6.236943109962288e-05 | 2.30% | 2.35% | 1.02x | ✅ |
| `clamp[within-bounds]` | 7.001520536240415e-05 | 7.297235258817885e-05 | -4.22% | -4.05% | 0.96x | ❌ |
