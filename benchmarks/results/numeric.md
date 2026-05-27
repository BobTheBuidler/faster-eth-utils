#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.702593363734093e-05 | 7.229523949300752e-05 | -7.86% | -7.29% | 0.93x | ❌ |
| `clamp[at-lower]` | 7.018291157447544e-05 | 7.166405171892265e-05 | -2.11% | -2.07% | 0.98x | ❌ |
| `clamp[at-upper]` | 6.833174470442872e-05 | 7.140764156389335e-05 | -4.50% | -4.31% | 0.96x | ❌ |
| `clamp[below-lower]` | 6.197935595262123e-05 | 6.572945747292341e-05 | -6.05% | -5.71% | 0.94x | ❌ |
| `clamp[within-bounds]` | 6.951445167274327e-05 | 7.333667107339033e-05 | -5.50% | -5.21% | 0.95x | ❌ |
