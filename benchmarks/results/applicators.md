#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.715652706627768e-06 | 8.720753483565881e-06 | -13.03% | -11.53% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.871700464190321e-06 | 8.551663703742913e-06 | -8.64% | -7.95% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.769147407017061e-06 | 8.73569104975607e-06 | -12.44% | -11.06% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.742318525690885e-07 | 9.8845272025052e-07 | -1.46% | -1.44% | 0.99x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1734268503819456e-06 | 1.4179478070427863e-06 | -20.84% | -17.24% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.804895760626668e-06 | 4.826748261817852e-06 | -0.45% | -0.45% | 1.00x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.918371497534624e-06 | 6.213225627000443e-06 | -4.98% | -4.75% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.185362367228114e-06 | 5.429448479254495e-06 | -4.71% | -4.50% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0621057067029305e-05 | 5.427247195610155e-06 | 48.90% | 95.70% | 1.96x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0579549157256998e-05 | 4.726116275819855e-06 | 55.33% | 123.85% | 2.24x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.714800772592295e-06 | 5.872691529616286e-06 | 32.61% | 48.40% | 1.48x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.898079467127938e-06 | 6.148866026146263e-06 | 30.90% | 44.71% | 1.45x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.44222759688243e-06 | 6.610285552814745e-06 | 29.99% | 42.84% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.892583961542594e-06 | 7.120568558088454e-06 | 28.02% | 38.93% | 1.39x | ✅ |
| `apply_key_map[empty]` | 1.4518087335774872e-05 | 8.400321834810042e-06 | 42.14% | 72.83% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.756801525563038e-05 | 1.0365443432274428e-05 | 41.00% | 69.49% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.0141035712155458e-05 | 1.1937046056852521e-05 | 40.73% | 68.73% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.914011965038547e-05 | 1.1180300965129759e-05 | 41.59% | 71.20% | 1.71x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6542037232152032e-06 | 1.549324893580351e-06 | 6.34% | 6.77% | 1.07x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2953813247825133e-06 | 1.907491358182072e-06 | 16.90% | 20.34% | 1.20x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003720840806645081 | 0.001483414139682639 | -298.68% | -74.92% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005630673261336944 | 0.0017388436767864692 | -208.82% | -67.62% | 0.32x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046470209959242247 | 0.0018067049607141021 | -288.79% | -74.28% | 0.26x | ❌ |
