#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.005609807575225e-05 | 7.646827556397393e-05 | -9.15% | -8.39% | 0.92x | ❌ |
| `clamp[at-lower]` | 6.813697699129834e-05 | 7.449374051668315e-05 | -9.33% | -8.53% | 0.91x | ❌ |
| `clamp[at-upper]` | 6.85350338552165e-05 | 7.498197398642778e-05 | -9.41% | -8.60% | 0.91x | ❌ |
| `clamp[below-lower]` | 6.620088732800294e-05 | 6.509838039486954e-05 | 1.67% | 1.69% | 1.02x | ✅ |
| `clamp[within-bounds]` | 6.627674882151094e-05 | 7.682518983834113e-05 | -15.92% | -13.73% | 0.86x | ❌ |
