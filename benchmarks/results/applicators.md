#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.690334393214401e-06 | 8.467860738835862e-06 | -10.11% | -9.18% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.682992636959248e-06 | 8.582945027645744e-06 | -11.71% | -10.49% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.619711002667684e-06 | 8.542411578591394e-06 | -12.11% | -10.80% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.877741948272446e-07 | 1.060452844326393e-06 | -7.36% | -6.85% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1488769607170968e-06 | 1.4918234042308877e-06 | -29.85% | -22.99% | 0.77x | ❌ |
| `apply_formatter_to_array[empty]` | 4.747501556137104e-06 | 4.835553923858572e-06 | -1.85% | -1.82% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.893312422124577e-06 | 6.061840001377646e-06 | -2.86% | -2.78% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.140845755670813e-06 | 5.300382726606662e-06 | -3.10% | -3.01% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0388314316222289e-05 | 5.376765085536569e-06 | 48.24% | 93.21% | 1.93x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0468565934632005e-05 | 4.841431364332033e-06 | 53.75% | 116.23% | 2.16x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.863710573811296e-06 | 5.645961937956379e-06 | 36.30% | 56.99% | 1.57x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.843496897964894e-06 | 6.058812790870617e-06 | 31.49% | 45.96% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.411960639483696e-06 | 6.406188126420786e-06 | 31.94% | 46.92% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.8745949115977e-06 | 6.907579617333689e-06 | 30.05% | 42.95% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.429742596083202e-05 | 8.165927181497512e-06 | 42.89% | 75.09% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.7562494185786743e-05 | 1.0044416573714333e-05 | 42.81% | 74.85% | 1.75x | ✅ |
| `apply_key_map[two-keys]` | 2.0026685510099875e-05 | 1.1560097759399291e-05 | 42.28% | 73.24% | 1.73x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8971419918390518e-05 | 1.0939199050395732e-05 | 42.34% | 73.43% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5528301788187835e-06 | 1.5656248028363064e-06 | -0.82% | -0.82% | 0.99x | ❌ |
| `apply_one_of_formatters[second-matches]` | 2.1444338875001894e-06 | 1.8921006255771628e-06 | 11.77% | 13.34% | 1.13x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037393739140946075 | 0.0014290294261542595 | -282.16% | -73.83% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005568568919476173 | 0.0016420172190150133 | -194.87% | -66.09% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004600589315561485 | 0.0017135685151005008 | -272.47% | -73.15% | 0.27x | ❌ |
