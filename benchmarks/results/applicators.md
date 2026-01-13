#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.715958852154302e-06 | 8.554178111546513e-06 | -10.86% | -9.80% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.71223021887493e-06 | 8.735046702585567e-06 | -13.26% | -11.71% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.819099252358938e-06 | 8.731014071637506e-06 | -11.66% | -10.44% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.92238367222156e-07 | 9.851889098785153e-07 | 0.71% | 0.72% | 1.01x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1769255134486293e-06 | 1.4313653157843803e-06 | -21.62% | -17.78% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.915741697687381e-06 | 4.83318870881156e-06 | 1.68% | 1.71% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.958279997764004e-06 | 6.2032022177988275e-06 | -4.11% | -3.95% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.291437709677208e-06 | 5.461850015084928e-06 | -3.22% | -3.12% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0569467218793593e-05 | 5.308666529162306e-06 | 49.77% | 99.10% | 1.99x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.063766578006738e-05 | 4.699380763540137e-06 | 55.82% | 126.36% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.4125898259305e-06 | 5.8907757711869206e-06 | 29.98% | 42.81% | 1.43x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.944563521017594e-06 | 6.458949751611778e-06 | 27.79% | 38.48% | 1.38x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.530386771900689e-06 | 6.657356908474249e-06 | 30.15% | 43.16% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0010404563445706e-05 | 7.151987067928004e-06 | 28.55% | 39.97% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.434021750099433e-05 | 8.156199225609986e-06 | 43.12% | 75.82% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.7589957255614416e-05 | 1.027500250742291e-05 | 41.59% | 71.19% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.998486944336536e-05 | 1.1869044652944615e-05 | 40.61% | 68.38% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9127403808471255e-05 | 1.1115255452373884e-05 | 41.89% | 72.08% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.564597154791382e-06 | 1.5593549487866995e-06 | 0.34% | 0.34% | 1.00x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.178443856732818e-06 | 1.941229517522127e-06 | 10.89% | 12.22% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037985912638321864 | 0.0013359975747316087 | -251.71% | -71.57% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005528670046985462 | 0.0015638208310304312 | -182.86% | -64.65% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004540896437494204 | 0.001629871174254906 | -258.93% | -72.14% | 0.28x | ❌ |
