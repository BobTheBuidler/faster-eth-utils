#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.848602660836615e-06 | 8.917517883720301e-06 | -13.62% | -11.99% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.883317898477235e-06 | 9.018994990778031e-06 | -14.41% | -12.59% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.933491524846639e-06 | 8.896984788845222e-06 | -12.14% | -10.83% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.450533130182994e-07 | 9.89869213162996e-07 | -4.74% | -4.53% | 0.95x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1358681350923767e-06 | 1.409100418498604e-06 | -24.05% | -19.39% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 4.9455343013066295e-06 | 5.120921245625964e-06 | -3.55% | -3.42% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.965926383657239e-06 | 6.3998460346527965e-06 | -7.27% | -6.78% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.249316602644379e-06 | 5.633506126012144e-06 | -7.32% | -6.82% | 0.93x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0291760680490714e-05 | 5.059225945042699e-06 | 50.84% | 103.43% | 2.03x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.972609459826553e-06 | 4.635376604528437e-06 | 53.52% | 115.14% | 2.15x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.399563110394655e-06 | 5.650236752100742e-06 | 32.73% | 48.66% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.810317254297737e-06 | 5.986632501881563e-06 | 32.05% | 47.17% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.44139479159496e-06 | 6.451701407611155e-06 | 31.67% | 46.34% | 1.46x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.926125321552282e-06 | 6.894201944862134e-06 | 30.54% | 43.98% | 1.44x | ✅ |
| `apply_key_map[empty]` | 1.4359452237769105e-05 | 8.288070386378815e-06 | 42.28% | 73.25% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.702707557469923e-05 | 9.976215689082943e-06 | 41.41% | 70.68% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9204195448971604e-05 | 1.1328115167703167e-05 | 41.01% | 69.53% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.846850521079087e-05 | 1.058939711439177e-05 | 42.66% | 74.41% | 1.74x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6766683617479151e-06 | 1.5012269210091266e-06 | 10.46% | 11.69% | 1.12x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.243330161730755e-06 | 1.8461415169033088e-06 | 17.71% | 21.51% | 1.22x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036054433412340724 | 0.0014333169291599996 | -297.54% | -74.85% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005553631345068926 | 0.0015893773089169624 | -186.19% | -65.06% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045893539484742217 | 0.001738694607655353 | -278.85% | -73.60% | 0.26x | ❌ |
