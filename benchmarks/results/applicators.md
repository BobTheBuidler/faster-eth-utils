#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.682971351844704e-06 | 8.487184045469315e-06 | -10.47% | -9.48% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.752013660302254e-06 | 8.603795518567821e-06 | -10.99% | -9.90% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.667039129773645e-06 | 8.627486127964146e-06 | -12.53% | -11.13% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.76433614429939e-07 | 1.0058734279613666e-06 | -3.02% | -2.93% | 0.97x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1679412039306344e-06 | 1.4067588280698935e-06 | -20.45% | -16.98% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.856890444205959e-06 | 4.836948526982923e-06 | 0.41% | 0.41% | 1.00x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.952628061368663e-06 | 6.192998385153858e-06 | -4.04% | -3.88% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.293342472943288e-06 | 5.502304183327767e-06 | -3.95% | -3.80% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0609050312792127e-05 | 5.242163905692596e-06 | 50.59% | 102.38% | 2.02x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0712793446188441e-05 | 4.701400709374019e-06 | 56.11% | 127.86% | 2.28x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.444292643201312e-06 | 5.678998552468139e-06 | 32.75% | 48.69% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.026616229741502e-06 | 6.06476272237468e-06 | 32.81% | 48.84% | 1.49x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.511065392965066e-06 | 6.560427107508071e-06 | 31.02% | 44.98% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0152631017173723e-05 | 7.0037525957131965e-06 | 31.02% | 44.96% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.4944821236826875e-05 | 8.785744098166116e-06 | 41.21% | 70.10% | 1.70x | ✅ |
| `apply_key_map[single-key]` | 1.8046364744060926e-05 | 1.0540324596666163e-05 | 41.59% | 71.21% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 2.0340868651267163e-05 | 1.24411598123699e-05 | 38.84% | 63.50% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9431686482422473e-05 | 1.1585274541140088e-05 | 40.38% | 67.73% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5529133633667965e-06 | 1.549513475713809e-06 | 0.22% | 0.22% | 1.00x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1456280968815585e-06 | 1.9107041800226307e-06 | 10.95% | 12.30% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003718370518610803 | 0.001423384624428819 | -282.80% | -73.88% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005623651046190882 | 0.0015888967642406673 | -182.54% | -64.61% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004608421163831185 | 0.0016791046967733058 | -264.36% | -72.55% | 0.27x | ❌ |
