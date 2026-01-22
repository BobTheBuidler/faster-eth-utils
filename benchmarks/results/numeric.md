#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.8995284530475996e-05 | 5.9731380353219225e-05 | -1.25% | -1.23% | 0.99x | ❌ |
| `clamp[at-lower]` | 5.9081063246438115e-05 | 5.958341053561525e-05 | -0.85% | -0.84% | 0.99x | ❌ |
| `clamp[at-upper]` | 5.910859394696476e-05 | 5.931358164935978e-05 | -0.35% | -0.35% | 1.00x | ❌ |
| `clamp[below-lower]` | 5.2296602785649915e-05 | 5.2902683650183315e-05 | -1.16% | -1.15% | 0.99x | ❌ |
| `clamp[within-bounds]` | 5.9170575387392135e-05 | 6.002709926411484e-05 | -1.45% | -1.43% | 0.99x | ❌ |
