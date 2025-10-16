#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.958439620442342e-06 | 8.332871285099018e-06 | -4.70% | -4.49% | 0.96x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.94663817099599e-06 | 8.257908735042586e-06 | -3.92% | -3.77% | 0.96x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.895650293075344e-06 | 8.315588024671331e-06 | -5.32% | -5.05% | 0.95x | ❌ |
| `apply_formatter_if[condition-false]` | 9.79869742573091e-07 | 9.527673979607958e-07 | 2.77% | 2.84% | 1.03x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2263129910384352e-06 | 1.4248307590191182e-06 | -16.19% | -13.93% | 0.86x | ❌ |
| `apply_formatter_to_array[empty]` | 4.891709771494341e-06 | 4.823457124714465e-06 | 1.40% | 1.42% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.118853639806883e-06 | 6.220792246692727e-06 | -1.67% | -1.64% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.340053737584772e-06 | 5.426105976044148e-06 | -1.61% | -1.59% | 0.98x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0261128836888465e-05 | 7.419243218258427e-06 | 27.70% | 38.30% | 1.38x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.70939428624252e-06 | 6.6535179503217345e-06 | 31.47% | 45.93% | 1.46x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.735722449769047e-06 | 5.5153137035824484e-06 | 36.86% | 58.39% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.163344015270142e-06 | 5.917200435206802e-06 | 35.43% | 54.86% | 1.55x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.779859827951948e-06 | 6.391866038885762e-06 | 34.64% | 53.00% | 1.53x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.001002307649361e-05 | 6.817301682888622e-06 | 31.90% | 46.83% | 1.47x | ✅ |
| `apply_key_map[empty]` | 1.4589302158968292e-05 | 6.550297975163886e-06 | 55.10% | 122.73% | 2.23x | ✅ |
| `apply_key_map[single-key]` | 1.7047558832950548e-05 | 8.172064348708114e-06 | 52.06% | 108.61% | 2.09x | ✅ |
| `apply_key_map[two-keys]` | 1.9268780705994914e-05 | 9.642313976321657e-06 | 49.96% | 99.84% | 2.00x | ✅ |
| `apply_key_map[unrelated-key]` | 1.809704884605613e-05 | 8.866429478903185e-06 | 51.01% | 104.11% | 2.04x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6723169014041311e-06 | 1.516093764611404e-06 | 9.34% | 10.30% | 1.10x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2734344340098627e-06 | 1.8128421098433733e-06 | 20.26% | 25.41% | 1.25x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003610581900176858 | 0.0012987702012208116 | -259.71% | -72.20% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005723940575691164 | 0.0015406169495830327 | -169.15% | -62.85% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004783895444291523 | 0.0015090814601519998 | -215.45% | -68.30% | 0.32x | ❌ |
