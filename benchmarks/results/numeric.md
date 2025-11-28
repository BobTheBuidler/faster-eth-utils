#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.159090041976601e-05 | 6.781429767014081e-05 | 5.28% | 5.57% | 1.06x | ✅ |
| `clamp[at-lower]` | 7.102825755439487e-05 | 6.651381267126121e-05 | 6.36% | 6.79% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.128269408580498e-05 | 6.758025153672938e-05 | 5.19% | 5.48% | 1.05x | ✅ |
| `clamp[below-lower]` | 6.607017802137012e-05 | 6.055794089499934e-05 | 8.34% | 9.10% | 1.09x | ✅ |
| `clamp[within-bounds]` | 7.027243780186501e-05 | 6.972418241511177e-05 | 0.78% | 0.79% | 1.01x | ✅ |
