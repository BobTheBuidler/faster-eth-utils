#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.868428442859918e-05 | 7.191598983185551e-05 | -4.71% | -4.49% | 0.96x | ❌ |
| `clamp[at-lower]` | 6.720559435608048e-05 | 7.33777454735398e-05 | -9.18% | -8.41% | 0.92x | ❌ |
| `clamp[at-upper]` | 6.740555413779753e-05 | 7.094375184853006e-05 | -5.25% | -4.99% | 0.95x | ❌ |
| `clamp[below-lower]` | 6.264178253492468e-05 | 6.299341109600768e-05 | -0.56% | -0.56% | 0.99x | ❌ |
| `clamp[within-bounds]` | 6.69717305033397e-05 | 7.19648362469637e-05 | -7.46% | -6.94% | 0.93x | ❌ |
