#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.082678713484127e-06 | 9.123770702918326e-06 | -12.88% | -11.41% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.04698125854952e-06 | 9.071609664437136e-06 | -12.73% | -11.29% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.97534034037283e-06 | 9.084608600134425e-06 | -13.91% | -12.21% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.484956498183526e-07 | 9.636637205463044e-07 | -1.60% | -1.57% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1595584293541072e-06 | 1.4510508283328769e-06 | -25.14% | -20.09% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 4.887147851912869e-06 | 5.289946141379218e-06 | -8.24% | -7.61% | 0.92x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.940033536805008e-06 | 6.515261753958122e-06 | -9.68% | -8.83% | 0.91x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.340134409756515e-06 | 5.708556166069734e-06 | -6.90% | -6.45% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0599892303605743e-05 | 5.252489787871166e-06 | 50.45% | 101.81% | 2.02x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0175004492722485e-05 | 4.6982919685212065e-06 | 53.83% | 116.57% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.59426978611721e-06 | 6.115663013887622e-06 | 28.84% | 40.53% | 1.41x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.009668100181762e-06 | 6.328486436925455e-06 | 29.76% | 42.37% | 1.42x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.670950047086684e-06 | 6.746138361933562e-06 | 30.24% | 43.36% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0019961939531688e-05 | 7.049779475310041e-06 | 29.64% | 42.13% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4691430045055556e-05 | 8.368103213120258e-06 | 43.04% | 75.56% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.7837259886811797e-05 | 1.0506052642172997e-05 | 41.10% | 69.78% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 1.990405775083574e-05 | 1.1954000218092367e-05 | 39.94% | 66.51% | 1.67x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8732875183137935e-05 | 1.123697376668498e-05 | 40.01% | 66.71% | 1.67x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5922781195955081e-06 | 1.5076655401254563e-06 | 5.31% | 5.61% | 1.06x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.063778267133945e-06 | 1.8373413383686414e-06 | 10.97% | 12.32% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003792418526449276 | 0.0014629167125000287 | -285.75% | -74.08% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005735771801928642 | 0.0016790995885327211 | -192.74% | -65.84% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046448712273011635 | 0.0017966726876026341 | -286.81% | -74.15% | 0.26x | ❌ |
