#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.208669039017328e-05 | 6.669235056889465e-05 | 7.48% | 8.09% | 1.08x | ✅ |
| `clamp[at-lower]` | 7.213346682013494e-05 | 6.49053742247346e-05 | 10.02% | 11.14% | 1.11x | ✅ |
| `clamp[at-upper]` | 7.342333276837196e-05 | 6.550786115267756e-05 | 10.78% | 12.08% | 1.12x | ✅ |
| `clamp[below-lower]` | 7.026486674993997e-05 | 5.6104162576973866e-05 | 20.15% | 25.24% | 1.25x | ✅ |
| `clamp[within-bounds]` | 7.284334682462048e-05 | 6.523653499240516e-05 | 10.44% | 11.66% | 1.12x | ✅ |
