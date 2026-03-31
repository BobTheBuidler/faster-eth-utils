#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.851115601775143e-06 | 8.730767380278346e-06 | -11.20% | -10.08% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.846706734938295e-06 | 8.601133347041848e-06 | -9.61% | -8.77% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.805267207617434e-06 | 8.564583079028507e-06 | -9.73% | -8.87% | 0.91x | ❌ |
| `apply_formatter_if[condition-false]` | 9.46112609740783e-07 | 1.0108140021400786e-06 | -6.84% | -6.40% | 0.94x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1635850863792339e-06 | 1.43869636778626e-06 | -23.64% | -19.12% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 4.954206608112168e-06 | 4.954816053656969e-06 | -0.01% | -0.01% | 1.00x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.995796859784138e-06 | 6.3008184568412646e-06 | -5.09% | -4.84% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.261333041357494e-06 | 5.478969857264651e-06 | -4.14% | -3.97% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0457761841294169e-05 | 5.23755900769971e-06 | 49.92% | 99.67% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.005617009117973e-05 | 4.668131288749675e-06 | 53.58% | 115.42% | 2.15x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.31569294932976e-06 | 5.669855736739346e-06 | 31.82% | 46.66% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.750630720801647e-06 | 5.980680781755011e-06 | 31.65% | 46.31% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.470507215040885e-06 | 6.405337380023996e-06 | 32.37% | 47.85% | 1.48x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.893298450808578e-06 | 6.877025152603094e-06 | 30.49% | 43.86% | 1.44x | ✅ |
| `apply_key_map[empty]` | 1.4473687275928033e-05 | 8.140845709432762e-06 | 43.75% | 77.79% | 1.78x | ✅ |
| `apply_key_map[single-key]` | 1.699627881736897e-05 | 9.74786017409351e-06 | 42.65% | 74.36% | 1.74x | ✅ |
| `apply_key_map[two-keys]` | 1.9572786299393226e-05 | 1.1114474784024205e-05 | 43.21% | 76.10% | 1.76x | ✅ |
| `apply_key_map[unrelated-key]` | 1.82992387046864e-05 | 1.0264203473855713e-05 | 43.91% | 78.28% | 1.78x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7072901061706926e-06 | 1.4992972535866155e-06 | 12.18% | 13.87% | 1.14x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.188020582975677e-06 | 1.8393411087890827e-06 | 15.94% | 18.96% | 1.19x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.000356626609356205 | 0.001391619458399659 | -290.22% | -74.37% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005521912445649976 | 0.0015728115847603915 | -184.83% | -64.89% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004572320449177561 | 0.0016471427334347037 | -260.24% | -72.24% | 0.28x | ❌ |
