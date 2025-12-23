#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.202082604940961e-06 | 7.722964507112305e-06 | -7.23% | -6.74% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.165805055567454e-06 | 7.866130309730636e-06 | -9.77% | -8.90% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.185606830415243e-06 | 7.72882059868235e-06 | -7.56% | -7.03% | 0.93x | ❌ |
| `apply_formatter_if[condition-false]` | 8.715718570692943e-07 | 9.488657745139301e-07 | -8.87% | -8.15% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.0572738411957664e-06 | 1.4188666609529136e-06 | -34.20% | -25.48% | 0.75x | ❌ |
| `apply_formatter_to_array[empty]` | 4.508354197215196e-06 | 4.550253900495344e-06 | -0.93% | -0.92% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.496637789708569e-06 | 5.930353488149507e-06 | -7.89% | -7.31% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.820660237624137e-06 | 5.022966540310325e-06 | -4.20% | -4.03% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 9.064728585780744e-06 | 4.8587939114541355e-06 | 46.40% | 86.56% | 1.87x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.847595430223968e-06 | 4.333543163286292e-06 | 51.02% | 104.17% | 2.04x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.063584342180558e-06 | 5.049161787296442e-06 | 37.38% | 59.70% | 1.60x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.477754417708124e-06 | 5.648141151376609e-06 | 33.38% | 50.10% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.089911809573702e-06 | 6.0348066132450995e-06 | 33.61% | 50.62% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.663570167750342e-06 | 6.452431589719062e-06 | 33.23% | 49.77% | 1.50x | ✅ |
| `apply_key_map[empty]` | 1.2954258951144756e-05 | 8.54867051424906e-06 | 34.01% | 51.54% | 1.52x | ✅ |
| `apply_key_map[single-key]` | 1.5257864680024037e-05 | 9.73865641380778e-06 | 36.17% | 56.67% | 1.57x | ✅ |
| `apply_key_map[two-keys]` | 1.7365101226835e-05 | 1.1291390855409264e-05 | 34.98% | 53.79% | 1.54x | ✅ |
| `apply_key_map[unrelated-key]` | 1.6470288289507243e-05 | 1.059759269256749e-05 | 35.66% | 55.42% | 1.55x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.4283236368825365e-06 | 1.493828301542455e-06 | -4.59% | -4.39% | 0.96x | ❌ |
| `apply_one_of_formatters[second-matches]` | 1.9457583938906757e-06 | 1.8406275527750506e-06 | 5.40% | 5.71% | 1.06x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003425825956144306 | 0.0010347843734484134 | -202.05% | -66.89% | 0.33x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0004982342672260619 | 0.00116307078561713 | -133.44% | -57.16% | 0.43x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00040663771028020743 | 0.00131800197542057 | -224.12% | -69.15% | 0.31x | ❌ |
