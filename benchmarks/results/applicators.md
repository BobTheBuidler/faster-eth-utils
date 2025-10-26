#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.950942024222668e-06 | 8.696327378238145e-06 | -9.37% | -8.57% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.078386176894102e-06 | 8.677595952848399e-06 | -7.42% | -6.91% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.009405663057767e-06 | 8.5568553016451e-06 | -6.84% | -6.40% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 9.727234579906663e-07 | 9.380991395530411e-07 | 3.56% | 3.69% | 1.04x | ✅ |
| `apply_formatter_if[condition-true]` | 1.179062779483794e-06 | 1.430742210572674e-06 | -21.35% | -17.59% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.961910474687587e-06 | 4.748606519045663e-06 | 4.30% | 4.49% | 1.04x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.003769736243222e-06 | 6.015931418097192e-06 | -0.20% | -0.20% | 1.00x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.242092288661964e-06 | 5.283252542229679e-06 | -0.79% | -0.78% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.058514027170837e-05 | 4.96022600398208e-06 | 53.14% | 113.40% | 2.13x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0246335099537835e-05 | 4.474084669332909e-06 | 56.33% | 129.02% | 2.29x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.656907862265214e-06 | 5.483516090475841e-06 | 36.66% | 57.87% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.004488185876382e-06 | 5.882109814042292e-06 | 34.68% | 53.08% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.439127776179769e-06 | 6.313835668386514e-06 | 33.11% | 49.50% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.782553674443394e-06 | 6.730048813770091e-06 | 31.20% | 45.36% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.5447250532716443e-05 | 8.331789490432815e-06 | 46.06% | 85.40% | 1.85x | ✅ |
| `apply_key_map[single-key]` | 1.7224648907550116e-05 | 1.0084100606952255e-05 | 41.46% | 70.81% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9380746229049423e-05 | 1.167510966243685e-05 | 39.76% | 66.00% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8304611067023624e-05 | 1.0562965750615275e-05 | 42.29% | 73.29% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6267107909592244e-06 | 1.5118570175301273e-06 | 7.06% | 7.60% | 1.08x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.234272320714097e-06 | 1.8532024055403514e-06 | 17.06% | 20.56% | 1.21x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00034470498047133844 | 0.0013136570076345616 | -281.10% | -73.76% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005666138363636157 | 0.0015742045940759332 | -177.83% | -64.01% | 0.36x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046359902398166266 | 0.0015498740080509513 | -234.31% | -70.09% | 0.30x | ❌ |
