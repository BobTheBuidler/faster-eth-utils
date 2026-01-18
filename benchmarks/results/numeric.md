#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.628114958218263e-05 | 6.994981118962046e-05 | 8.30% | 9.05% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.27562188562562e-05 | 7.123614972458949e-05 | 2.09% | 2.13% | 1.02x | ✅ |
| `clamp[at-upper]` | 7.320571097030843e-05 | 7.07442661925336e-05 | 3.36% | 3.48% | 1.03x | ✅ |
| `clamp[below-lower]` | 6.95902875946847e-05 | 6.110943813084019e-05 | 12.19% | 13.88% | 1.14x | ✅ |
| `clamp[within-bounds]` | 7.607752627678726e-05 | 6.978974134693824e-05 | 8.26% | 9.01% | 1.09x | ✅ |
