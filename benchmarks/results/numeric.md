#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.384808910892326e-05 | 6.86570295408558e-05 | 7.03% | 7.56% | 1.08x | ✅ |
| `clamp[at-lower]` | 7.639086613236955e-05 | 7.020580324494892e-05 | 8.10% | 8.81% | 1.09x | ✅ |
| `clamp[at-upper]` | 7.36908807641427e-05 | 6.822814535095398e-05 | 7.41% | 8.01% | 1.08x | ✅ |
| `clamp[below-lower]` | 6.842227071575017e-05 | 6.260862028144996e-05 | 8.50% | 9.29% | 1.09x | ✅ |
| `clamp[within-bounds]` | 7.355546128194582e-05 | 6.725238414467305e-05 | 8.57% | 9.37% | 1.09x | ✅ |
