#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.83724999604058e-06 | 8.83964676066931e-06 | -12.79% | -11.34% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.934053928259565e-06 | 8.886753412669538e-06 | -12.01% | -10.72% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.911364491406154e-06 | 9.02874760827752e-06 | -14.12% | -12.38% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.430780983534462e-07 | 9.476686578334817e-07 | -0.49% | -0.48% | 1.00x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1968599028910763e-06 | 1.4438975226137588e-06 | -20.64% | -17.11% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 5.062983661685541e-06 | 5.188946543369881e-06 | -2.49% | -2.43% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.169767106011747e-06 | 6.557778239479635e-06 | -6.29% | -5.92% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.420350725470245e-06 | 6.021181880421972e-06 | -11.08% | -9.98% | 0.90x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0387817324533776e-05 | 5.590717165340646e-06 | 46.18% | 85.80% | 1.86x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.979958809749535e-06 | 5.067980624875369e-06 | 49.22% | 96.92% | 1.97x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.747862863359625e-06 | 5.945031240454083e-06 | 32.04% | 47.15% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.233116662611417e-06 | 6.340710278561701e-06 | 31.33% | 45.62% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.838393313512457e-06 | 6.7962195235630465e-06 | 30.92% | 44.76% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0254190753614929e-05 | 7.192473061026685e-06 | 29.86% | 42.57% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.4661988458828854e-05 | 9.010966813097647e-06 | 38.54% | 62.71% | 1.63x | ✅ |
| `apply_key_map[single-key]` | 1.747019029620192e-05 | 1.1039321666350452e-05 | 36.81% | 58.25% | 1.58x | ✅ |
| `apply_key_map[two-keys]` | 1.955527794705726e-05 | 1.2555746744390308e-05 | 35.79% | 55.75% | 1.56x | ✅ |
| `apply_key_map[unrelated-key]` | 1.864887805246821e-05 | 1.1649043867081472e-05 | 37.53% | 60.09% | 1.60x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6505290144011456e-06 | 1.4826889414365415e-06 | 10.17% | 11.32% | 1.11x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.175506367619827e-06 | 1.867746578230409e-06 | 14.15% | 16.48% | 1.16x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003271261187730262 | 0.0013917771632055858 | -325.46% | -76.50% | 0.24x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005923433537744194 | 0.0014770754610490561 | -149.36% | -59.90% | 0.40x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004762235390239945 | 0.001369909057403957 | -187.66% | -65.24% | 0.35x | ❌ |
