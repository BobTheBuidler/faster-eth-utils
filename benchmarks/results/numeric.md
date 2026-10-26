#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.917299436048425e-05 | 7.082220092781977e-05 | -2.38% | -2.33% | 0.98x | ❌ |
| `clamp[at-lower]` | 6.6441377942853e-05 | 7.16401344245738e-05 | -7.82% | -7.26% | 0.93x | ❌ |
| `clamp[at-upper]` | 6.719981986463476e-05 | 6.952096948510613e-05 | -3.45% | -3.34% | 0.97x | ❌ |
| `clamp[below-lower]` | 6.221811304956912e-05 | 6.20876747193605e-05 | 0.21% | 0.21% | 1.00x | ✅ |
| `clamp[within-bounds]` | 6.525705993728254e-05 | 7.245226390501994e-05 | -11.03% | -9.93% | 0.90x | ❌ |
