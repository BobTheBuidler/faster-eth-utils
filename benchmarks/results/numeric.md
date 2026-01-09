#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.604581544336226e-05 | 6.700718612534711e-05 | 11.89% | 13.49% | 1.13x | ✅ |
| `clamp[at-lower]` | 7.316166657646598e-05 | 6.504049274974171e-05 | 11.10% | 12.49% | 1.12x | ✅ |
| `clamp[at-upper]` | 7.321603932067482e-05 | 6.567501009030523e-05 | 10.30% | 11.48% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.89406452843991e-05 | 5.904510544412414e-05 | 14.35% | 16.76% | 1.17x | ✅ |
| `clamp[within-bounds]` | 7.395485493791074e-05 | 6.584524212949644e-05 | 10.97% | 12.32% | 1.12x | ✅ |
