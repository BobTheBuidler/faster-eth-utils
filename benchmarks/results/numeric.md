#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.9119026094169923e-05 | 6.209833446981555e-05 | -5.04% | -4.80% | 0.95x | ❌ |
| `clamp[at-lower]` | 5.926402415825272e-05 | 6.194925459383592e-05 | -4.53% | -4.33% | 0.96x | ❌ |
| `clamp[at-upper]` | 5.9373257187773366e-05 | 6.161345968884997e-05 | -3.77% | -3.64% | 0.96x | ❌ |
| `clamp[below-lower]` | 5.2379919757652935e-05 | 5.4885932037599166e-05 | -4.78% | -4.57% | 0.95x | ❌ |
| `clamp[within-bounds]` | 5.906071918829595e-05 | 6.207215416960926e-05 | -5.10% | -4.85% | 0.95x | ❌ |
