#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.71790604321427e-06 | 8.542607879936389e-06 | -10.69% | -9.65% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.748619435208e-06 | 8.580655859670041e-06 | -10.74% | -9.70% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.756910379397054e-06 | 8.579371436099125e-06 | -10.60% | -9.59% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.631881050384954e-07 | 1.0327372860008784e-06 | -7.22% | -6.73% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1486178925097442e-06 | 1.4738267321660453e-06 | -28.31% | -22.07% | 0.78x | ❌ |
| `apply_formatter_to_array[empty]` | 4.759546152860723e-06 | 4.791191933405141e-06 | -0.66% | -0.66% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.887960146758076e-06 | 6.1219405447338205e-06 | -3.97% | -3.82% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.173253585753874e-06 | 5.417224743991167e-06 | -4.72% | -4.50% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0644906437654531e-05 | 5.403139377960207e-06 | 49.24% | 97.01% | 1.97x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0725090686159254e-05 | 4.801378860890397e-06 | 55.23% | 123.38% | 2.23x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.44279654307191e-06 | 5.556752127450677e-06 | 34.18% | 51.94% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.980678048493124e-06 | 5.929068501274078e-06 | 33.98% | 51.47% | 1.51x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.41779156426279e-06 | 6.367380689258288e-06 | 32.39% | 47.91% | 1.48x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.88860445138936e-06 | 6.7988021829778586e-06 | 31.25% | 45.45% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.4393974950027738e-05 | 8.124857487149295e-06 | 43.55% | 77.16% | 1.77x | ✅ |
| `apply_key_map[single-key]` | 1.757248851470064e-05 | 1.0221268537397012e-05 | 41.83% | 71.92% | 1.72x | ✅ |
| `apply_key_map[two-keys]` | 1.984863537541309e-05 | 1.1623634385766132e-05 | 41.44% | 70.76% | 1.71x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9266630668416828e-05 | 1.0859671074752202e-05 | 43.63% | 77.41% | 1.77x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6749813349676402e-06 | 1.4986108060609122e-06 | 10.53% | 11.77% | 1.12x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1770335867275036e-06 | 1.8295233499205502e-06 | 15.96% | 18.99% | 1.19x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038600546924419827 | 0.001367857327744438 | -254.36% | -71.78% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005546785654313524 | 0.001600681211878996 | -188.58% | -65.35% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004548288507205814 | 0.001674113809603993 | -268.08% | -72.83% | 0.27x | ❌ |
