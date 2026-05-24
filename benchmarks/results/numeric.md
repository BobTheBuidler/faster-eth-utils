#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.973058208361775e-05 | 7.61016376194343e-05 | -9.14% | -8.37% | 0.92x | ❌ |
| `clamp[at-lower]` | 6.998046472294222e-05 | 7.548265611857845e-05 | -7.86% | -7.29% | 0.93x | ❌ |
| `clamp[at-upper]` | 7.066037893966111e-05 | 7.545299807945614e-05 | -6.78% | -6.35% | 0.94x | ❌ |
| `clamp[below-lower]` | 6.238544386391983e-05 | 6.61423781793092e-05 | -6.02% | -5.68% | 0.94x | ❌ |
| `clamp[within-bounds]` | 6.891578349592129e-05 | 7.556850888847855e-05 | -9.65% | -8.80% | 0.91x | ❌ |
