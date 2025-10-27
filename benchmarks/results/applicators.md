#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.968918861374269e-06 | 8.632180299522135e-06 | -8.32% | -7.68% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.88357053744239e-06 | 8.462298284448514e-06 | -7.34% | -6.84% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.007991892723118e-06 | 8.335067147065425e-06 | -4.08% | -3.92% | 0.96x | ❌ |
| `apply_formatter_if[condition-false]` | 9.832241701190674e-07 | 9.255769807012341e-07 | 5.86% | 6.23% | 1.06x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2096494346586774e-06 | 1.4327226658315564e-06 | -18.44% | -15.57% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.847399023770937e-06 | 4.932810232872515e-06 | -1.76% | -1.73% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.046970178295292e-06 | 6.280711400402569e-06 | -3.87% | -3.72% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.26624849578621e-06 | 5.4379217207009546e-06 | -3.26% | -3.16% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0175754843798085e-05 | 4.943500858783067e-06 | 51.42% | 105.84% | 2.06x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.781210664580918e-06 | 4.405324356669887e-06 | 54.96% | 122.03% | 2.22x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.708582554679413e-06 | 5.400561355363324e-06 | 37.99% | 61.25% | 1.61x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.090438012815286e-06 | 5.8396761530190756e-06 | 35.76% | 55.67% | 1.56x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.686519784824249e-06 | 6.298349181645657e-06 | 34.98% | 53.79% | 1.54x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0057726540722213e-05 | 6.742033969867135e-06 | 32.97% | 49.18% | 1.49x | ✅ |
| `apply_key_map[empty]` | 1.4844175932336252e-05 | 8.612898594765737e-06 | 41.98% | 72.35% | 1.72x | ✅ |
| `apply_key_map[single-key]` | 1.6963542800683917e-05 | 1.0518567493749011e-05 | 37.99% | 61.27% | 1.61x | ✅ |
| `apply_key_map[two-keys]` | 1.942500709178432e-05 | 1.2059527375680733e-05 | 37.92% | 61.08% | 1.61x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8329105996476756e-05 | 1.0983966135662044e-05 | 40.07% | 66.87% | 1.67x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7232576199118293e-06 | 1.5145591907614191e-06 | 12.11% | 13.78% | 1.14x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.21904419285966e-06 | 1.9528838964699207e-06 | 11.99% | 13.63% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036983501467814146 | 0.0013090617817311054 | -253.96% | -71.75% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005700907149761083 | 0.001577677382760479 | -176.74% | -63.87% | 0.36x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004788142830073961 | 0.0015398039295568006 | -221.59% | -68.90% | 0.31x | ❌ |
