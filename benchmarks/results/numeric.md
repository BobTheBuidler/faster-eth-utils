#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.543216985465705e-05 | 6.540551719013409e-05 | 13.29% | 15.33% | 1.15x | ✅ |
| `clamp[at-lower]` | 7.242717559583917e-05 | 6.790732352922403e-05 | 6.24% | 6.66% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.199216212584446e-05 | 6.396256213128036e-05 | 11.15% | 12.55% | 1.13x | ✅ |
| `clamp[below-lower]` | 6.908096268455052e-05 | 5.777067047531909e-05 | 16.37% | 19.58% | 1.20x | ✅ |
| `clamp[within-bounds]` | 7.38783327310273e-05 | 6.591232276617907e-05 | 10.78% | 12.09% | 1.12x | ✅ |
