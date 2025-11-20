#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.884919519701544e-06 | 8.560605055094712e-06 | -8.57% | -7.89% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.739345746884427e-06 | 8.541864595308311e-06 | -10.37% | -9.40% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.82628822351414e-06 | 8.529540212541073e-06 | -8.99% | -8.24% | 0.92x | ❌ |
| `apply_formatter_if[condition-false]` | 9.778771532789333e-07 | 9.003444351676906e-07 | 7.93% | 8.61% | 1.09x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1761020298933086e-06 | 1.3232861841410924e-06 | -12.51% | -11.12% | 0.89x | ❌ |
| `apply_formatter_to_array[empty]` | 4.9481864883606315e-06 | 4.8327062959236996e-06 | 2.33% | 2.39% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.294841016096183e-06 | 6.254458277631719e-06 | 0.64% | 0.65% | 1.01x | ✅ |
| `apply_formatter_to_array[single-item]` | 5.3645953288703436e-06 | 5.446765502835366e-06 | -1.53% | -1.51% | 0.98x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0077819987267546e-05 | 4.975013874918696e-06 | 50.63% | 102.57% | 2.03x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.666393453999899e-06 | 4.5218502116696666e-06 | 53.22% | 113.77% | 2.14x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.658771538746387e-06 | 5.5387464764046366e-06 | 36.03% | 56.33% | 1.56x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.99318304186788e-06 | 5.837503502408179e-06 | 35.09% | 54.06% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.607032202238532e-06 | 6.305734388646797e-06 | 34.36% | 52.35% | 1.52x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.7931742141149e-06 | 6.894117629189906e-06 | 29.60% | 42.05% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4987094207479346e-05 | 8.48703658130117e-06 | 43.37% | 76.59% | 1.77x | ✅ |
| `apply_key_map[single-key]` | 1.7325005983708267e-05 | 9.995501798081972e-06 | 42.31% | 73.33% | 1.73x | ✅ |
| `apply_key_map[two-keys]` | 1.9357357368674866e-05 | 1.1419721754966237e-05 | 41.01% | 69.51% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8097878940887303e-05 | 1.0850852357120473e-05 | 40.04% | 66.79% | 1.67x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6745980289597926e-06 | 1.4319387304638084e-06 | 14.49% | 16.95% | 1.17x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2409905003973957e-06 | 1.7824072753238316e-06 | 20.46% | 25.73% | 1.26x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038408306413356463 | 0.001365356843226844 | -255.48% | -71.87% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006176151958974848 | 0.0015150762857125582 | -145.31% | -59.24% | 0.41x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004953150849973153 | 0.0014276571371605194 | -188.23% | -65.31% | 0.35x | ❌ |
