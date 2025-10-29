#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.164788011404114e-05 | 7.151139112647984e-05 | 0.19% | 0.19% | 1.00x | ✅ |
| `clamp[at-lower]` | 7.009836003906954e-05 | 6.974363705510383e-05 | 0.51% | 0.51% | 1.01x | ✅ |
| `clamp[at-upper]` | 7.172377686656705e-05 | 6.947175078088256e-05 | 3.14% | 3.24% | 1.03x | ✅ |
| `clamp[below-lower]` | 6.645796902879361e-05 | 6.121266716803724e-05 | 7.89% | 8.57% | 1.09x | ✅ |
| `clamp[within-bounds]` | 6.98429300108893e-05 | 6.903255351830367e-05 | 1.16% | 1.17% | 1.01x | ✅ |
