#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.26637923710105e-05 | 7.179697369236091e-05 | 1.19% | 1.21% | 1.01x | ✅ |
| `clamp[at-lower]` | 7.117268544947209e-05 | 6.984218885104235e-05 | 1.87% | 1.91% | 1.02x | ✅ |
| `clamp[at-upper]` | 7.10103727070354e-05 | 7.081236463593347e-05 | 0.28% | 0.28% | 1.00x | ✅ |
| `clamp[below-lower]` | 6.760193484595785e-05 | 6.157246340063084e-05 | 8.92% | 9.79% | 1.10x | ✅ |
| `clamp[within-bounds]` | 6.967296639318407e-05 | 6.965601701146916e-05 | 0.02% | 0.02% | 1.00x | ✅ |
