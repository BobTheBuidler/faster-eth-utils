#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.69224364844315e-06 | 8.465386556186758e-06 | -10.05% | -9.13% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.650976756507925e-06 | 8.599093416490045e-06 | -12.39% | -11.03% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.573503000313737e-06 | 8.689369201684232e-06 | -14.73% | -12.84% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0022293695958233e-06 | 9.95937098530229e-07 | 0.63% | 0.63% | 1.01x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1739275919958013e-06 | 1.413296043241695e-06 | -20.39% | -16.94% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.762358771944145e-06 | 4.8962561007737074e-06 | -2.81% | -2.73% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.935630121804327e-06 | 6.228587397273971e-06 | -4.94% | -4.70% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.171720925774378e-06 | 5.474442777513278e-06 | -5.85% | -5.53% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0916742255590865e-05 | 5.299771438535618e-06 | 51.45% | 105.99% | 2.06x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.1070247394831557e-05 | 4.795337971418599e-06 | 56.68% | 130.85% | 2.31x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.598195423263704e-06 | 5.7185594909951316e-06 | 33.49% | 50.36% | 1.50x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.107178561171375e-06 | 6.083985223951172e-06 | 33.20% | 49.69% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.703145237542232e-06 | 6.560539320501261e-06 | 32.39% | 47.90% | 1.48x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.837740649768115e-06 | 7.028596992823987e-06 | 28.55% | 39.97% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.4949994593322804e-05 | 8.214382449313783e-06 | 45.05% | 82.00% | 1.82x | ✅ |
| `apply_key_map[single-key]` | 1.8050497799861e-05 | 1.0189775699050384e-05 | 43.55% | 77.14% | 1.77x | ✅ |
| `apply_key_map[two-keys]` | 2.055827252680881e-05 | 1.1911779739335638e-05 | 42.06% | 72.59% | 1.73x | ✅ |
| `apply_key_map[unrelated-key]` | 1.950499688854819e-05 | 1.0875518041488445e-05 | 44.24% | 79.35% | 1.79x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5967530354198352e-06 | 1.5689994408701155e-06 | 1.74% | 1.77% | 1.02x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1390973246790837e-06 | 1.916052757857711e-06 | 10.43% | 11.64% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036442240071952244 | 0.0014414268957701891 | -295.54% | -74.72% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005555042050153347 | 0.0016252877796053848 | -192.58% | -65.82% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004620773108650381 | 0.0017102161361500835 | -270.11% | -72.98% | 0.27x | ❌ |
