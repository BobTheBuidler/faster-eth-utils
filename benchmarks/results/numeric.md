#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.609745313592172e-05 | 7.702055524992512e-05 | -1.21% | -1.20% | 0.99x | ❌ |
| `clamp[at-lower]` | 7.664668903134574e-05 | 7.598721338662462e-05 | 0.86% | 0.87% | 1.01x | ✅ |
| `clamp[at-upper]` | 7.536327847000751e-05 | 7.585892293844017e-05 | -0.66% | -0.65% | 0.99x | ❌ |
| `clamp[below-lower]` | 6.863479079635665e-05 | 6.874135630562423e-05 | -0.16% | -0.16% | 1.00x | ❌ |
| `clamp[within-bounds]` | 7.583501221195861e-05 | 8.034402006429199e-05 | -5.95% | -5.61% | 0.94x | ❌ |
