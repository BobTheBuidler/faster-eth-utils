#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.2929602033248575e-06 | 8.340819364777146e-06 | -14.37% | -12.56% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.352619656505639e-06 | 8.397866462696304e-06 | -14.22% | -12.45% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.331801026009306e-06 | 8.296639286086878e-06 | -13.16% | -11.63% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.451582760441731e-07 | 9.801887476645013e-07 | -3.71% | -3.57% | 0.96x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2035295111331921e-06 | 1.3968088237275086e-06 | -16.06% | -13.84% | 0.86x | ❌ |
| `apply_formatter_to_array[empty]` | 4.882911565512142e-06 | 4.641791384788491e-06 | 4.94% | 5.19% | 1.05x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.027426627826417e-06 | 6.009826183880155e-06 | 0.29% | 0.29% | 1.00x | ✅ |
| `apply_formatter_to_array[single-item]` | 5.27451234950828e-06 | 5.206581842584586e-06 | 1.29% | 1.30% | 1.01x | ✅ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0054301786991468e-05 | 4.893595495679107e-06 | 51.33% | 105.46% | 2.05x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.727750428382805e-06 | 4.394911652690794e-06 | 54.82% | 121.34% | 2.21x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.190279017715646e-06 | 5.287401725841985e-06 | 35.44% | 54.90% | 1.55x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.618724174581713e-06 | 5.606852527701634e-06 | 34.95% | 53.72% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.2175859083821e-06 | 6.079551173260393e-06 | 34.04% | 51.62% | 1.52x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.561265251146943e-06 | 6.421242825183314e-06 | 32.84% | 48.90% | 1.49x | ✅ |
| `apply_key_map[empty]` | 1.4562107213676771e-05 | 8.392294288867698e-06 | 42.37% | 73.52% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.7039570355371602e-05 | 9.958717942782498e-06 | 41.56% | 71.10% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9040211246010197e-05 | 1.1258518113818751e-05 | 40.87% | 69.12% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8761535543969084e-05 | 1.0835287164723895e-05 | 42.25% | 73.15% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6208454124145216e-06 | 1.4806034055637413e-06 | 8.65% | 9.47% | 1.09x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.181633405570031e-06 | 1.8872000677715052e-06 | 13.50% | 15.60% | 1.16x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0002929805942764086 | 0.0009782904729539244 | -233.91% | -70.05% | 0.30x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0004591107077181816 | 0.0013459755685998219 | -193.17% | -65.89% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00036288362771625093 | 0.0010964256218371532 | -202.14% | -66.90% | 0.33x | ❌ |
