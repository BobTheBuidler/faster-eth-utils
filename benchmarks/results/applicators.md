#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.91741970962904e-06 | 9.061849405623485e-06 | -14.45% | -12.63% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.970005672571047e-06 | 9.061815636744993e-06 | -13.70% | -12.05% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.103236517845662e-06 | 8.845655600240541e-06 | -9.16% | -8.39% | 0.92x | ❌ |
| `apply_formatter_if[condition-false]` | 9.665725928850786e-07 | 9.773196903923785e-07 | -1.11% | -1.10% | 0.99x | ❌ |
| `apply_formatter_if[condition-true]` | 1.132335915322633e-06 | 1.4231745447804146e-06 | -25.68% | -20.44% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 4.899565108097019e-06 | 5.261168047357492e-06 | -7.38% | -6.87% | 0.93x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.989279876254988e-06 | 6.42092587510543e-06 | -7.21% | -6.72% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.300651535507653e-06 | 5.597717501782349e-06 | -5.60% | -5.31% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0213431954907724e-05 | 5.311802251321436e-06 | 47.99% | 92.28% | 1.92x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0011492945845709e-05 | 4.883058152592396e-06 | 51.23% | 105.03% | 2.05x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.543661477266117e-06 | 5.78128041892673e-06 | 32.33% | 47.78% | 1.48x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.87555637054249e-06 | 6.1236738381002875e-06 | 31.01% | 44.94% | 1.45x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.51873076324765e-06 | 6.739370255729016e-06 | 29.20% | 41.24% | 1.41x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.897287757857488e-06 | 6.74062078134994e-06 | 31.89% | 46.83% | 1.47x | ✅ |
| `apply_key_map[empty]` | 1.4309464338228181e-05 | 8.336125458040655e-06 | 41.74% | 71.66% | 1.72x | ✅ |
| `apply_key_map[single-key]` | 1.699978130071644e-05 | 1.0046493353917621e-05 | 40.90% | 69.21% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 1.8718979770981753e-05 | 1.1530772031355872e-05 | 38.40% | 62.34% | 1.62x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8388072637164625e-05 | 1.0835143078131568e-05 | 41.08% | 69.71% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.578283975960462e-06 | 1.5766417483066976e-06 | 0.10% | 0.10% | 1.00x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.192599890430552e-06 | 1.950733017908414e-06 | 11.03% | 12.40% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003607783295168261 | 0.0014375109590293107 | -298.45% | -74.90% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005588255511479705 | 0.0016565742118647665 | -196.44% | -66.27% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045877528699251257 | 0.00177892486986316 | -287.76% | -74.21% | 0.26x | ❌ |
