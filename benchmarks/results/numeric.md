#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.57230681909648e-05 | 6.60088360095094e-05 | 12.83% | 14.72% | 1.15x | ✅ |
| `clamp[at-lower]` | 7.1671069323484e-05 | 6.702487651208138e-05 | 6.48% | 6.93% | 1.07x | ✅ |
| `clamp[at-upper]` | 7.225344472584346e-05 | 6.538742179549949e-05 | 9.50% | 10.50% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.858933870655711e-05 | 5.732789278659356e-05 | 16.42% | 19.64% | 1.20x | ✅ |
| `clamp[within-bounds]` | 7.186927767004882e-05 | 6.706084417890828e-05 | 6.69% | 7.17% | 1.07x | ✅ |
