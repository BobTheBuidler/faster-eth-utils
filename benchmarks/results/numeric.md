#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.453316547959066e-05 | 6.836199877142982e-05 | 8.28% | 9.03% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.126090884844208e-05 | 6.881505743160343e-05 | 3.43% | 3.55% | 1.04x | ✅ |
| `clamp[at-upper]` | 7.163401581442049e-05 | 6.961542788493675e-05 | 2.82% | 2.90% | 1.03x | ✅ |
| `clamp[below-lower]` | 6.676038239519085e-05 | 6.09155830460369e-05 | 8.75% | 9.59% | 1.10x | ✅ |
| `clamp[within-bounds]` | 7.058131806988982e-05 | 6.910706052596349e-05 | 2.09% | 2.13% | 1.02x | ✅ |
