#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.5940128225171515e-06 | 8.555479003270361e-06 | -12.66% | -11.24% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.672581706293188e-06 | 8.653758567736347e-06 | -12.79% | -11.34% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.483879102439341e-06 | 8.56281468627595e-06 | -14.42% | -12.60% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0085684231201903e-06 | 1.0625848011151383e-06 | -5.36% | -5.08% | 0.95x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1737243507454387e-06 | 1.5541192950109893e-06 | -32.41% | -24.48% | 0.76x | ❌ |
| `apply_formatter_to_array[empty]` | 4.949854692215062e-06 | 4.892582797101193e-06 | 1.16% | 1.17% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.025596622208886e-06 | 6.212934359258443e-06 | -3.11% | -3.02% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.351566041916219e-06 | 5.389501778319521e-06 | -0.71% | -0.70% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0419983189408036e-05 | 5.305804526720663e-06 | 49.08% | 96.39% | 1.96x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0556820283018844e-05 | 4.8285080022599735e-06 | 54.26% | 118.64% | 2.19x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.36605264541366e-06 | 5.6624088414149474e-06 | 32.32% | 47.75% | 1.48x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.830695171575778e-06 | 5.95230248810701e-06 | 32.60% | 48.36% | 1.48x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.373485042430006e-06 | 6.412393709794549e-06 | 31.59% | 46.18% | 1.46x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.831493369970224e-06 | 6.995780416788681e-06 | 28.84% | 40.53% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.434264705763846e-05 | 8.28485837787785e-06 | 42.24% | 73.12% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.7544479218654037e-05 | 1.0243153988165303e-05 | 41.62% | 71.28% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9970006911250777e-05 | 1.1736569410689688e-05 | 41.23% | 70.15% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9048592196575927e-05 | 1.100818819091217e-05 | 42.21% | 73.04% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6029463319233057e-06 | 1.575797952023875e-06 | 1.69% | 1.72% | 1.02x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1840803416949458e-06 | 1.921662533411571e-06 | 12.02% | 13.66% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0004015775167646049 | 0.001377450139143906 | -243.01% | -70.85% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005497147427053902 | 0.001559370468354633 | -183.67% | -64.75% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00047405765683476334 | 0.001673691338484818 | -253.06% | -71.68% | 0.28x | ❌ |
