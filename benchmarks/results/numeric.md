#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.388655512767235e-05 | 6.752775056468543e-05 | 8.61% | 9.42% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.45179830373927e-05 | 6.650445244602608e-05 | 10.75% | 12.05% | 1.12x | ✅ |
| `clamp[at-upper]` | 7.291525019777164e-05 | 6.842307172602871e-05 | 6.16% | 6.57% | 1.07x | ✅ |
| `clamp[below-lower]` | 6.855774242637916e-05 | 5.867695424360003e-05 | 14.41% | 16.84% | 1.17x | ✅ |
| `clamp[within-bounds]` | 7.125998072962883e-05 | 6.776841283763655e-05 | 4.90% | 5.15% | 1.05x | ✅ |
