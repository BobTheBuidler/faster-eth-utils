#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.063814069915244e-05 | 6.689948263333744e-05 | 5.29% | 5.59% | 1.06x | ✅ |
| `clamp[at-lower]` | 7.432353575282708e-05 | 6.768397539507464e-05 | 8.93% | 9.81% | 1.10x | ✅ |
| `clamp[at-upper]` | 7.115531456574077e-05 | 6.655849759768862e-05 | 6.46% | 6.91% | 1.07x | ✅ |
| `clamp[below-lower]` | 6.57609611723459e-05 | 5.854786052215632e-05 | 10.97% | 12.32% | 1.12x | ✅ |
| `clamp[within-bounds]` | 7.0131702066208e-05 | 6.767883442829744e-05 | 3.50% | 3.62% | 1.04x | ✅ |
