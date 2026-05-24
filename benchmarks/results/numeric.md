#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.469118232140966e-05 | 7.892244469049888e-05 | -5.67% | -5.36% | 0.95x | ❌ |
| `clamp[at-lower]` | 7.495201276316328e-05 | 7.863478146661708e-05 | -4.91% | -4.68% | 0.95x | ❌ |
| `clamp[at-upper]` | 7.507192983042808e-05 | 7.940240703695412e-05 | -5.77% | -5.45% | 0.95x | ❌ |
| `clamp[below-lower]` | 6.678722822503164e-05 | 6.789653962743536e-05 | -1.66% | -1.63% | 0.98x | ❌ |
| `clamp[within-bounds]` | 7.465922272945977e-05 | 8.041685112907157e-05 | -7.71% | -7.16% | 0.93x | ❌ |
