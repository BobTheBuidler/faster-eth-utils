#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.556559847545497e-05 | 6.70215990271114e-05 | 11.31% | 12.75% | 1.13x | ✅ |
| `clamp[at-lower]` | 7.321282821970858e-05 | 6.597966078035413e-05 | 9.88% | 10.96% | 1.11x | ✅ |
| `clamp[at-upper]` | 7.498783765547536e-05 | 6.657108131081084e-05 | 11.22% | 12.64% | 1.13x | ✅ |
| `clamp[below-lower]` | 6.956043645306273e-05 | 5.8790900313180356e-05 | 15.48% | 18.32% | 1.18x | ✅ |
| `clamp[within-bounds]` | 7.417611476610069e-05 | 6.696216360867435e-05 | 9.73% | 10.77% | 1.11x | ✅ |
