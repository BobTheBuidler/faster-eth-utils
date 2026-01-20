#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.535674422783721e-05 | 6.977542519340889e-05 | 7.41% | 8.00% | 1.08x | ✅ |
| `clamp[at-lower]` | 7.696363785685463e-05 | 6.837785287194303e-05 | 11.16% | 12.56% | 1.13x | ✅ |
| `clamp[at-upper]` | 7.799982495809558e-05 | 6.774954430068504e-05 | 13.14% | 15.13% | 1.15x | ✅ |
| `clamp[below-lower]` | 6.980965597343483e-05 | 6.682877164999408e-05 | 4.27% | 4.46% | 1.04x | ✅ |
| `clamp[within-bounds]` | 7.430906380579146e-05 | 7.051188049702086e-05 | 5.11% | 5.39% | 1.05x | ✅ |
