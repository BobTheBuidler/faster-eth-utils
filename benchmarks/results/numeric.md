#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.647670170894244e-05 | 7.504538069049574e-05 | -12.89% | -11.42% | 0.89x | ❌ |
| `clamp[at-lower]` | 6.60803489904951e-05 | 7.164800842937497e-05 | -8.43% | -7.77% | 0.92x | ❌ |
| `clamp[at-upper]` | 6.558404707737015e-05 | 7.202950205460077e-05 | -9.83% | -8.95% | 0.91x | ❌ |
| `clamp[below-lower]` | 6.161495620410142e-05 | 6.566761598117695e-05 | -6.58% | -6.17% | 0.94x | ❌ |
| `clamp[within-bounds]` | 6.903565738785484e-05 | 7.497758697486655e-05 | -8.61% | -7.92% | 0.92x | ❌ |
