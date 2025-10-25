#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.061161907577074e-05 | 7.019858860560258e-05 | 0.58% | 0.59% | 1.01x | ✅ |
| `clamp[at-lower]` | 6.874222078385669e-05 | 6.889319622371743e-05 | -0.22% | -0.22% | 1.00x | ❌ |
| `clamp[at-upper]` | 6.997724350298677e-05 | 6.866362370957244e-05 | 1.88% | 1.91% | 1.02x | ✅ |
| `clamp[below-lower]` | 6.65592581789103e-05 | 6.074339947108631e-05 | 8.74% | 9.57% | 1.10x | ✅ |
| `clamp[within-bounds]` | 6.912341450417344e-05 | 7.050692473434173e-05 | -2.00% | -1.96% | 0.98x | ❌ |
