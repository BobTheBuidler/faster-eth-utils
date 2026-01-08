#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.487756693037678e-05 | 6.860573394087338e-05 | 8.38% | 9.14% | 1.09x | ✅ |
| `clamp[at-lower]` | 7.353982832636642e-05 | 6.716336335418739e-05 | 8.67% | 9.49% | 1.09x | ✅ |
| `clamp[at-upper]` | 7.333190878384628e-05 | 6.476517210318463e-05 | 11.68% | 13.23% | 1.13x | ✅ |
| `clamp[below-lower]` | 6.871464002289501e-05 | 5.848649856846578e-05 | 14.88% | 17.49% | 1.17x | ✅ |
| `clamp[within-bounds]` | 7.295975313487424e-05 | 6.743385581980068e-05 | 7.57% | 8.19% | 1.08x | ✅ |
