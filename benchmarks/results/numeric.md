#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.563979312744935e-05 | 6.95006233072998e-05 | 8.12% | 8.83% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.375920495464723e-05 | 7.003442928701058e-05 | 5.05% | 5.32% | 1.05x | ✅ |
| `clamp[at-upper]` | 7.332518593248114e-05 | 6.846640959416103e-05 | 6.63% | 7.10% | 1.07x | ✅ |
| `clamp[below-lower]` | 7.0010799912606e-05 | 6.148342570351781e-05 | 12.18% | 13.87% | 1.14x | ✅ |
| `clamp[within-bounds]` | 7.427082953419836e-05 | 6.971160763030291e-05 | 6.14% | 6.54% | 1.07x | ✅ |
