#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.584261327491332e-06 | 8.416882608717718e-06 | -10.98% | -9.89% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.6096188742059125e-06 | 8.404413380067621e-06 | -10.44% | -9.46% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.603969039635617e-06 | 8.642521754966607e-06 | -13.66% | -12.02% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.802806430663514e-07 | 9.800699619426472e-07 | 0.02% | 0.02% | 1.00x | ✅ |
| `apply_formatter_if[condition-true]` | 1.184796369239279e-06 | 1.4166631332267892e-06 | -19.57% | -16.37% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.80440383798179e-06 | 4.689236125574479e-06 | 2.40% | 2.46% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.080104829528746e-06 | 6.13528446917468e-06 | -0.91% | -0.90% | 0.99x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.14768191800732e-06 | 5.412210600839266e-06 | -5.14% | -4.89% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0512445425223912e-05 | 5.354455134704081e-06 | 49.07% | 96.33% | 1.96x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0573763930519754e-05 | 4.838531669299547e-06 | 54.24% | 118.53% | 2.19x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.669687985107761e-06 | 5.708026714026737e-06 | 34.16% | 51.89% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.994877210174386e-06 | 5.977211517727103e-06 | 33.55% | 50.49% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.611963168025005e-06 | 6.579046264325578e-06 | 31.55% | 46.10% | 1.46x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0092788089264157e-05 | 7.070149005868224e-06 | 29.95% | 42.75% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.4566721263149796e-05 | 8.37656780819442e-06 | 42.50% | 73.90% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.7529919919818375e-05 | 1.0440407691575742e-05 | 40.44% | 67.90% | 1.68x | ✅ |
| `apply_key_map[two-keys]` | 1.9923967995996824e-05 | 1.1876050569807256e-05 | 40.39% | 67.77% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.887749248735822e-05 | 1.1212658491591626e-05 | 40.60% | 68.36% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6162454285672458e-06 | 1.5408481275405732e-06 | 4.66% | 4.89% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.232854669243261e-06 | 1.8992210408446763e-06 | 14.94% | 17.57% | 1.18x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036023874388082557 | 0.0013948545052000709 | -287.20% | -74.17% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005466834029948334 | 0.0015610610125598534 | -185.55% | -64.98% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045058913749225856 | 0.001620351144172208 | -259.61% | -72.19% | 0.28x | ❌ |
