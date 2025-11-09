#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.2402178129977e-05 | 7.20161509628032e-05 | 0.53% | 0.54% | 1.01x | ✅ |
| `clamp[at-lower]` | 7.216240402232012e-05 | 7.43026713836649e-05 | -2.97% | -2.88% | 0.97x | ❌ |
| `clamp[at-upper]` | 7.101459196217295e-05 | 7.215159706493084e-05 | -1.60% | -1.58% | 0.98x | ❌ |
| `clamp[below-lower]` | 6.612991475308718e-05 | 6.285744481168275e-05 | 4.95% | 5.21% | 1.05x | ✅ |
| `clamp[within-bounds]` | 7.163371073547751e-05 | 7.346669418963395e-05 | -2.56% | -2.49% | 0.98x | ❌ |
