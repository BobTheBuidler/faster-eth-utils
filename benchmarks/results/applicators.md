#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.617115272820042e-06 | 8.521720552018597e-06 | -11.88% | -10.62% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.731277460374791e-06 | 8.528438986434818e-06 | -10.31% | -9.35% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.735143497763571e-06 | 8.654558404875046e-06 | -11.89% | -10.62% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.921670688375675e-07 | 9.927724385511131e-07 | -0.06% | -0.06% | 1.00x | ❌ |
| `apply_formatter_if[condition-true]` | 1.182348734739063e-06 | 1.4178818069496765e-06 | -19.92% | -16.61% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.778560353945366e-06 | 4.823297475317298e-06 | -0.94% | -0.93% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.877241960177055e-06 | 6.173151596752055e-06 | -5.03% | -4.79% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.177079289033605e-06 | 5.381433402569379e-06 | -3.95% | -3.80% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0394039343429494e-05 | 5.248354672128862e-06 | 49.51% | 98.04% | 1.98x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0566344565547061e-05 | 4.706053158066171e-06 | 55.46% | 124.53% | 2.25x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.354169186219835e-06 | 5.703893216326969e-06 | 31.72% | 46.46% | 1.46x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.92385433149747e-06 | 6.040246121025559e-06 | 32.31% | 47.74% | 1.48x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.468182177454325e-06 | 6.566804026496363e-06 | 30.64% | 44.18% | 1.44x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.873148752050562e-06 | 7.0804537010629175e-06 | 28.29% | 39.44% | 1.39x | ✅ |
| `apply_key_map[empty]` | 1.4496031406849694e-05 | 8.350951848472171e-06 | 42.39% | 73.59% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.757480923318066e-05 | 1.0401588264557217e-05 | 40.82% | 68.96% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.0061294117545765e-05 | 1.1881400062345985e-05 | 40.77% | 68.85% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9272938543885436e-05 | 1.1025637938165552e-05 | 42.79% | 74.80% | 1.75x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5916404909255466e-06 | 1.550175324314786e-06 | 2.61% | 2.67% | 1.03x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1905081259130327e-06 | 1.925949928620727e-06 | 12.08% | 13.74% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003664923296634832 | 0.0014999848602820591 | -309.28% | -75.57% | 0.24x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006198984479814584 | 0.0016094573467094716 | -159.63% | -61.48% | 0.39x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005176280134582222 | 0.001773875370995447 | -242.69% | -70.82% | 0.29x | ❌ |
