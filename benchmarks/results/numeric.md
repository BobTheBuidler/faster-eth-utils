#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.845784111698041e-05 | 8.469542947640004e-05 | -23.72% | -19.17% | 0.81x | ❌ |
| `clamp[at-lower]` | 6.77126928106907e-05 | 8.530973226873421e-05 | -25.99% | -20.63% | 0.79x | ❌ |
| `clamp[at-upper]` | 6.864769021035615e-05 | 8.425336765297108e-05 | -22.73% | -18.52% | 0.81x | ❌ |
| `clamp[below-lower]` | 6.274802390465396e-05 | 7.69637091396749e-05 | -22.66% | -18.47% | 0.82x | ❌ |
| `clamp[within-bounds]` | 6.784230749483799e-05 | 8.559560119600465e-05 | -26.17% | -20.74% | 0.79x | ❌ |
