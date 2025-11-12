#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.06131856565953e-06 | 8.511312777599367e-06 | -5.58% | -5.29% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.195544429344e-06 | 8.470682884644804e-06 | -3.36% | -3.25% | 0.97x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.916058366735395e-06 | 8.451046351465744e-06 | -6.76% | -6.33% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 9.532692618688296e-07 | 9.514615307110738e-07 | 0.19% | 0.19% | 1.00x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1880948523095508e-06 | 1.4316193195227977e-06 | -20.50% | -17.01% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 5.005028518872543e-06 | 4.778208445608025e-06 | 4.53% | 4.75% | 1.05x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.259978701589554e-06 | 6.344645076498637e-06 | -1.35% | -1.33% | 0.99x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.454360728227258e-06 | 5.462270389269613e-06 | -0.15% | -0.14% | 1.00x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.043989562678013e-05 | 5.075259345174338e-06 | 51.39% | 105.70% | 2.06x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0004461681828855e-05 | 4.613660561859722e-06 | 53.88% | 116.84% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.436470477460366e-06 | 5.5890215784686925e-06 | 33.75% | 50.95% | 1.51x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.132752910829445e-06 | 6.001879502194829e-06 | 34.28% | 52.16% | 1.52x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.893144276661485e-06 | 6.486187050126263e-06 | 34.44% | 52.53% | 1.53x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0045189860025204e-05 | 7.007973594094651e-06 | 30.24% | 43.34% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.5013224340552252e-05 | 8.587296853236073e-06 | 42.80% | 74.83% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.74180737080946e-05 | 1.003978228360288e-05 | 42.36% | 73.49% | 1.73x | ✅ |
| `apply_key_map[two-keys]` | 1.9676035884899967e-05 | 1.1411375002286217e-05 | 42.00% | 72.42% | 1.72x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8929455441647355e-05 | 1.070434820796284e-05 | 43.45% | 76.84% | 1.77x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.722502850496111e-06 | 1.5342646709339087e-06 | 10.93% | 12.27% | 1.12x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2572576692218985e-06 | 1.9364212156241415e-06 | 14.21% | 16.57% | 1.17x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038519423292694287 | 0.001384485744514858 | -259.43% | -72.18% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000598403567773157 | 0.0016116678316823126 | -169.33% | -62.87% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005007100343510757 | 0.0014312355274731787 | -185.84% | -65.02% | 0.35x | ❌ |
