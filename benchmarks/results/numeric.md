#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.319462871699862e-05 | 6.665401473526551e-05 | 8.94% | 9.81% | 1.10x | ✅ |
| `clamp[at-lower]` | 7.341829347226528e-05 | 6.588036008172191e-05 | 10.27% | 11.44% | 1.11x | ✅ |
| `clamp[at-upper]` | 7.262756063100868e-05 | 6.53787893551101e-05 | 9.98% | 11.09% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.750070689241921e-05 | 5.9314513749989336e-05 | 12.13% | 13.80% | 1.14x | ✅ |
| `clamp[within-bounds]` | 7.216475079758938e-05 | 6.73421081542132e-05 | 6.68% | 7.16% | 1.07x | ✅ |
