#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.774893294573612e-05 | 7.411511513648164e-05 | -9.40% | -8.59% | 0.91x | ❌ |
| `clamp[at-lower]` | 6.745867545969942e-05 | 7.25600668578643e-05 | -7.56% | -7.03% | 0.93x | ❌ |
| `clamp[at-upper]` | 6.88669301520974e-05 | 7.070718194526075e-05 | -2.67% | -2.60% | 0.97x | ❌ |
| `clamp[below-lower]` | 6.227346957488502e-05 | 6.623072706756535e-05 | -6.35% | -5.97% | 0.94x | ❌ |
| `clamp[within-bounds]` | 6.708695879013893e-05 | 7.288181001359439e-05 | -8.64% | -7.95% | 0.92x | ❌ |
