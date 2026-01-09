#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.682960273980992e-06 | 8.629445085266855e-06 | -12.32% | -10.97% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.702749459799181e-06 | 8.729783365283525e-06 | -13.33% | -11.76% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.665218719950512e-06 | 8.817596061578703e-06 | -15.03% | -13.07% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 9.346587412172169e-07 | 9.403676767475559e-07 | -0.61% | -0.61% | 0.99x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1038645361448715e-06 | 1.3767105977701214e-06 | -24.72% | -19.82% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 4.827003139575096e-06 | 4.8220253236853126e-06 | 0.10% | 0.10% | 1.00x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.863745730587954e-06 | 6.086722974767346e-06 | -3.80% | -3.66% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.185511160981119e-06 | 5.422887406560539e-06 | -4.58% | -4.38% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.04848761485151e-05 | 5.671780481030388e-06 | 45.91% | 84.86% | 1.85x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0670415483636575e-05 | 5.19276936707213e-06 | 51.33% | 105.49% | 2.05x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.781162803277034e-06 | 5.904196370261098e-06 | 32.76% | 48.73% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.30226586245519e-06 | 6.330112080940713e-06 | 31.95% | 46.95% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.806569099187899e-06 | 6.781735404151026e-06 | 30.84% | 44.60% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0081498378830562e-05 | 7.135170704122347e-06 | 29.23% | 41.29% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.436818071944943e-05 | 8.273916789231391e-06 | 42.42% | 73.66% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.748159069929378e-05 | 1.0325280379092809e-05 | 40.94% | 69.31% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 1.977292632056729e-05 | 1.1922477230938515e-05 | 39.70% | 65.85% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9009582057479086e-05 | 1.1100542269155625e-05 | 41.61% | 71.25% | 1.71x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5426087776700035e-06 | 1.5236095032637006e-06 | 1.23% | 1.25% | 1.01x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.0771234833806216e-06 | 1.8860018640463804e-06 | 9.20% | 10.13% | 1.10x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036550850858851246 | 0.0014717865045322895 | -302.67% | -75.17% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005551680062017658 | 0.0016720146718213038 | -201.17% | -66.80% | 0.33x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045307600970177856 | 0.0017682903355253792 | -290.29% | -74.38% | 0.26x | ❌ |
