#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.038076308696847e-06 | 8.32392493741855e-06 | -3.56% | -3.43% | 0.97x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.942673694686403e-06 | 8.35296753312687e-06 | -5.17% | -4.91% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.107767725130356e-06 | 8.460711182081474e-06 | -4.35% | -4.17% | 0.96x | ❌ |
| `apply_formatter_if[condition-false]` | 9.764681435246662e-07 | 9.378401593358765e-07 | 3.96% | 4.12% | 1.04x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1862930042078731e-06 | 1.3498913977123393e-06 | -13.79% | -12.12% | 0.88x | ❌ |
| `apply_formatter_to_array[empty]` | 5.060834723961358e-06 | 4.764630864695895e-06 | 5.85% | 6.22% | 1.06x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.156011129655193e-06 | 6.178515874805474e-06 | -0.37% | -0.36% | 1.00x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.376006679220652e-06 | 5.3866742968182156e-06 | -0.20% | -0.20% | 1.00x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0671403709411956e-05 | 5.035930711534707e-06 | 52.81% | 111.91% | 2.12x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0209098819519896e-05 | 4.509532332719645e-06 | 55.83% | 126.39% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.641500919952838e-06 | 5.629088942615054e-06 | 34.86% | 53.52% | 1.54x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.319512651020474e-06 | 6.059991178077542e-06 | 34.98% | 53.79% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.686293335968942e-06 | 6.417322451273918e-06 | 33.75% | 50.94% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.955292650119635e-06 | 6.746422598354244e-06 | 32.23% | 47.56% | 1.48x | ✅ |
| `apply_key_map[empty]` | 1.533443074207357e-05 | 8.53800358651809e-06 | 44.32% | 79.60% | 1.80x | ✅ |
| `apply_key_map[single-key]` | 1.7167395790004412e-05 | 1.0163911240389827e-05 | 40.80% | 68.91% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 1.9110554299981272e-05 | 1.158754268511499e-05 | 39.37% | 64.92% | 1.65x | ✅ |
| `apply_key_map[unrelated-key]` | 1.818908624288451e-05 | 1.0674414589041744e-05 | 41.31% | 70.40% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6455678590610433e-06 | 1.4831352927256512e-06 | 9.87% | 10.95% | 1.11x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.22514428405973e-06 | 1.8292928444324134e-06 | 17.79% | 21.64% | 1.22x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003790329545455078 | 0.001328838904476906 | -250.59% | -71.48% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005911426173463308 | 0.0015054025439474041 | -154.66% | -60.73% | 0.39x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004944680735381936 | 0.0013929085133525243 | -181.70% | -64.50% | 0.35x | ❌ |
