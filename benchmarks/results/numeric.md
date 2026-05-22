#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.783563998116243e-05 | 7.435012194766824e-05 | -9.60% | -8.76% | 0.91x | ❌ |
| `clamp[at-lower]` | 6.813267282697007e-05 | 7.487946108780768e-05 | -9.90% | -9.01% | 0.91x | ❌ |
| `clamp[at-upper]` | 6.754711993631198e-05 | 7.424933022633909e-05 | -9.92% | -9.03% | 0.91x | ❌ |
| `clamp[below-lower]` | 5.7871180392131146e-05 | 6.445056520093274e-05 | -11.37% | -10.21% | 0.90x | ❌ |
| `clamp[within-bounds]` | 6.940988206098546e-05 | 7.390062262625133e-05 | -6.47% | -6.08% | 0.94x | ❌ |
