#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.392621980530301e-06 | 8.46278466884686e-06 | -14.48% | -12.65% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.5454379510802106e-06 | 8.434245289333808e-06 | -11.78% | -10.54% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.311533890831634e-06 | 8.730123745743078e-06 | -19.40% | -16.25% | 0.84x | ❌ |
| `apply_formatter_if[condition-false]` | 9.83024680208378e-07 | 9.452417753197029e-07 | 3.84% | 4.00% | 1.04x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1627110445482958e-06 | 1.3935470764693083e-06 | -19.85% | -16.56% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.752237845153965e-06 | 4.69199599295055e-06 | 1.27% | 1.28% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.872847507879561e-06 | 6.071074983352002e-06 | -3.38% | -3.27% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.089248594616565e-06 | 5.2465197406634e-06 | -3.09% | -3.00% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0020836402074572e-05 | 5.198644096447285e-06 | 48.12% | 92.76% | 1.93x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.008046484884798e-05 | 4.699949811523545e-06 | 53.38% | 114.48% | 2.14x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.28583599562086e-06 | 5.6398072351108875e-06 | 31.93% | 46.92% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.734416350105603e-06 | 5.9271831752251255e-06 | 32.14% | 47.36% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.333624365284684e-06 | 6.5314246705254575e-06 | 30.02% | 42.90% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.634863994467411e-06 | 7.004320404873875e-06 | 27.30% | 37.56% | 1.38x | ✅ |
| `apply_key_map[empty]` | 1.3819223250045774e-05 | 8.189814344429313e-06 | 40.74% | 68.74% | 1.69x | ✅ |
| `apply_key_map[single-key]` | 1.6850332855311882e-05 | 1.0447820879997697e-05 | 38.00% | 61.28% | 1.61x | ✅ |
| `apply_key_map[two-keys]` | 1.8872016061596136e-05 | 1.1970215057791717e-05 | 36.57% | 57.66% | 1.58x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8685465355730236e-05 | 1.1389590977049038e-05 | 39.05% | 64.06% | 1.64x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5622826651907941e-06 | 1.4814077374248873e-06 | 5.18% | 5.46% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.157910529089097e-06 | 1.8918883017150115e-06 | 12.33% | 14.06% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037484785672476344 | 0.0013170199819815868 | -251.35% | -71.54% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005342906335359321 | 0.00150552505490737 | -181.78% | -64.51% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00044256037294026514 | 0.0015417119420293112 | -248.36% | -71.29% | 0.29x | ❌ |
