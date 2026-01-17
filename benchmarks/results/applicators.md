#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.6020597158935885e-06 | 8.415159081130076e-06 | -10.70% | -9.66% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.696896929114217e-06 | 8.49548158263803e-06 | -10.38% | -9.40% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.590084802850161e-06 | 8.563765276691983e-06 | -12.83% | -11.37% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.964864796118886e-07 | 9.87840299124016e-07 | 0.87% | 0.88% | 1.01x | ✅ |
| `apply_formatter_if[condition-true]` | 1.182910734010085e-06 | 1.4155569510690165e-06 | -19.67% | -16.43% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.758924114404652e-06 | 4.650154266421926e-06 | 2.29% | 2.34% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.905425195150984e-06 | 6.146474074847335e-06 | -4.08% | -3.92% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.148252580768149e-06 | 5.413144747130754e-06 | -5.15% | -4.89% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.054185135181033e-05 | 5.197059835408603e-06 | 50.70% | 102.84% | 2.03x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0498053639450075e-05 | 4.635248789392529e-06 | 55.85% | 126.48% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.395383423748813e-06 | 5.867754010996858e-06 | 30.11% | 43.08% | 1.43x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.845573634810665e-06 | 6.110350441130228e-06 | 30.92% | 44.76% | 1.45x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.440705543022155e-06 | 6.561735945891482e-06 | 30.50% | 43.88% | 1.44x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.849432188048778e-06 | 6.935284281188369e-06 | 29.59% | 42.02% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4389701517690222e-05 | 8.229074758209714e-06 | 42.81% | 74.86% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.7545342079364776e-05 | 1.0428074603038264e-05 | 40.56% | 68.25% | 1.68x | ✅ |
| `apply_key_map[two-keys]` | 2.0184402343069382e-05 | 1.1841804186612815e-05 | 41.33% | 70.45% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9127601218842884e-05 | 1.094363499120801e-05 | 42.79% | 74.78% | 1.75x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5974050749816607e-06 | 1.5402904124128115e-06 | 3.58% | 3.71% | 1.04x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.232619463112132e-06 | 1.8929266045206206e-06 | 15.21% | 17.95% | 1.18x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003815791927708923 | 0.001436460014308313 | -276.45% | -73.44% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000556658073787906 | 0.001627800447020352 | -192.42% | -65.80% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000458886555620938 | 0.001706096783605146 | -271.79% | -73.10% | 0.27x | ❌ |
