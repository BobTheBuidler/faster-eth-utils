#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.588339959635718e-05 | 6.86163225687027e-05 | 9.58% | 10.59% | 1.11x | ✅ |
| `clamp[at-lower]` | 7.463731989716062e-05 | 7.114340085787678e-05 | 4.68% | 4.91% | 1.05x | ✅ |
| `clamp[at-upper]` | 7.304645976982065e-05 | 6.77871639922353e-05 | 7.20% | 7.76% | 1.08x | ✅ |
| `clamp[below-lower]` | 6.816514135919663e-05 | 6.348111442083692e-05 | 6.87% | 7.38% | 1.07x | ✅ |
| `clamp[within-bounds]` | 7.599569615479874e-05 | 6.938184605104767e-05 | 8.70% | 9.53% | 1.10x | ✅ |
