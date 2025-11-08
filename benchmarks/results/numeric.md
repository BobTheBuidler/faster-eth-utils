#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.123142324875967e-05 | 6.779184650157768e-05 | 4.83% | 5.07% | 1.05x | ✅ |
| `clamp[at-lower]` | 7.12713938796722e-05 | 6.696429912753663e-05 | 6.04% | 6.43% | 1.06x | ✅ |
| `clamp[at-upper]` | 7.16710493242715e-05 | 6.783949897559471e-05 | 5.35% | 5.65% | 1.06x | ✅ |
| `clamp[below-lower]` | 6.637748114925166e-05 | 6.036997933040264e-05 | 9.05% | 9.95% | 1.10x | ✅ |
| `clamp[within-bounds]` | 7.046181900577531e-05 | 6.739833309863106e-05 | 4.35% | 4.55% | 1.05x | ✅ |
