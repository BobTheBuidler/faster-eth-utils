#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.690605659630948e-05 | 7.06271381178567e-05 | -5.56% | -5.27% | 0.95x | ❌ |
| `clamp[at-lower]` | 6.597862610040507e-05 | 7.37330058057164e-05 | -11.75% | -10.52% | 0.89x | ❌ |
| `clamp[at-upper]` | 6.589765414394635e-05 | 7.091971068035376e-05 | -7.62% | -7.08% | 0.93x | ❌ |
| `clamp[below-lower]` | 6.217799962381443e-05 | 6.299892526134729e-05 | -1.32% | -1.30% | 0.99x | ❌ |
| `clamp[within-bounds]` | 6.692291758887827e-05 | 7.067166132739206e-05 | -5.60% | -5.30% | 0.95x | ❌ |
