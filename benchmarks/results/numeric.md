#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.478419497159241e-05 | 6.856274294745293e-05 | 8.32% | 9.07% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.344817778279671e-05 | 7.050432085769764e-05 | 4.01% | 4.18% | 1.04x | ✅ |
| `clamp[at-upper]` | 7.303776513396588e-05 | 6.772573593708515e-05 | 7.27% | 7.84% | 1.08x | ✅ |
| `clamp[below-lower]` | 6.801881678868203e-05 | 6.0305102486311626e-05 | 11.34% | 12.79% | 1.13x | ✅ |
| `clamp[within-bounds]` | 7.459406865064986e-05 | 6.996844081003162e-05 | 6.20% | 6.61% | 1.07x | ✅ |
