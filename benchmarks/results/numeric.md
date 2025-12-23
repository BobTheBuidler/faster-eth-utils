#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.8864259687584734e-05 | 6.108390900958149e-05 | -3.77% | -3.63% | 0.96x | ❌ |
| `clamp[at-lower]` | 5.90882241542602e-05 | 6.108588647773437e-05 | -3.38% | -3.27% | 0.97x | ❌ |
| `clamp[at-upper]` | 5.9095508937487134e-05 | 6.064954757355148e-05 | -2.63% | -2.56% | 0.97x | ❌ |
| `clamp[below-lower]` | 5.238831714233007e-05 | 5.379219305928583e-05 | -2.68% | -2.61% | 0.97x | ❌ |
| `clamp[within-bounds]` | 5.92430568662237e-05 | 6.133410233586361e-05 | -3.53% | -3.41% | 0.97x | ❌ |
