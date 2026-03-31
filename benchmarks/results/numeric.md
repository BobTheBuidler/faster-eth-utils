#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.726620136345646e-05 | 6.952639734896953e-05 | -3.36% | -3.25% | 0.97x | ❌ |
| `clamp[at-lower]` | 6.827671877326294e-05 | 6.793346096646456e-05 | 0.50% | 0.51% | 1.01x | ✅ |
| `clamp[at-upper]` | 6.626227095916366e-05 | 7.028828921392573e-05 | -6.08% | -5.73% | 0.94x | ❌ |
| `clamp[below-lower]` | 6.029268679018853e-05 | 6.300321186606856e-05 | -4.50% | -4.30% | 0.96x | ❌ |
| `clamp[within-bounds]` | 6.721719672083879e-05 | 7.03860680506773e-05 | -4.71% | -4.50% | 0.95x | ❌ |
