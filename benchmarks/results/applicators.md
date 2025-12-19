#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.176489775008155e-06 | 7.69499965735152e-06 | -7.23% | -6.74% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.172088725069659e-06 | 7.745733972005484e-06 | -8.00% | -7.41% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.159798952531064e-06 | 7.653546427784574e-06 | -6.90% | -6.45% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 8.833680582129419e-07 | 9.612120312355384e-07 | -8.81% | -8.10% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.0651452063819713e-06 | 1.4095264202519518e-06 | -32.33% | -24.43% | 0.76x | ❌ |
| `apply_formatter_to_array[empty]` | 4.5620346278789865e-06 | 4.447232336532286e-06 | 2.52% | 2.58% | 1.03x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.552641192289321e-06 | 5.8439980440691945e-06 | -5.25% | -4.99% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.889104704220593e-06 | 4.901547599834785e-06 | -0.25% | -0.25% | 1.00x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 9.113688300713475e-06 | 4.824204295432356e-06 | 47.07% | 88.92% | 1.89x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.774590500570324e-06 | 4.311777947737195e-06 | 50.86% | 103.50% | 2.04x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 7.599837397983264e-06 | 4.9991363280331315e-06 | 34.22% | 52.02% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.190843335935046e-06 | 5.459785722359284e-06 | 33.34% | 50.02% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 8.784296510158062e-06 | 6.008404919289098e-06 | 31.60% | 46.20% | 1.46x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.227291741318124e-06 | 6.432414556722423e-06 | 30.29% | 43.45% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.2998506126587506e-05 | 7.730248418412921e-06 | 40.53% | 68.15% | 1.68x | ✅ |
| `apply_key_map[single-key]` | 1.5283207573880077e-05 | 9.261282296510786e-06 | 39.40% | 65.02% | 1.65x | ✅ |
| `apply_key_map[two-keys]` | 1.7427334644294657e-05 | 1.0720935103106463e-05 | 38.48% | 62.55% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.64713670718288e-05 | 9.951425693433445e-06 | 39.58% | 65.52% | 1.66x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.4201707723407152e-06 | 1.465818035526555e-06 | -3.21% | -3.11% | 0.97x | ❌ |
| `apply_one_of_formatters[second-matches]` | 1.931417157350986e-06 | 1.8322127077888145e-06 | 5.14% | 5.41% | 1.05x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003427818411952112 | 0.0010541728173801635 | -207.53% | -67.48% | 0.33x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00048709380232526663 | 0.0011660334883081484 | -139.39% | -58.23% | 0.42x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0003971832489565816 | 0.001404978190410861 | -253.74% | -71.73% | 0.28x | ❌ |
