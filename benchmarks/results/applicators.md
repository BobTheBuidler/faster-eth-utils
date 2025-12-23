#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.595355769186191e-06 | 8.535561939993204e-06 | -12.38% | -11.02% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.6109597409712695e-06 | 8.614106984985296e-06 | -13.18% | -11.65% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.593539774051521e-06 | 8.610859149299005e-06 | -13.40% | -11.81% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.544591547787163e-07 | 1.0451440379278853e-06 | -9.50% | -8.68% | 0.91x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1277625328944541e-06 | 1.4907762521529079e-06 | -32.19% | -24.35% | 0.76x | ❌ |
| `apply_formatter_to_array[empty]` | 4.73742603216884e-06 | 4.872240406501688e-06 | -2.85% | -2.77% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.86305529645431e-06 | 6.13159837668774e-06 | -4.58% | -4.38% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.095406225120555e-06 | 5.362481822468297e-06 | -5.24% | -4.98% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0791540645497576e-05 | 5.401992751976943e-06 | 49.94% | 99.77% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0812088790942552e-05 | 4.801671200347393e-06 | 55.59% | 125.17% | 2.25x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.760251329159001e-06 | 5.6972279833150385e-06 | 34.97% | 53.76% | 1.54x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.177178279996242e-06 | 6.065702476354516e-06 | 33.90% | 51.30% | 1.51x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.59154516945618e-06 | 6.744734582561321e-06 | 29.68% | 42.21% | 1.42x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.001712505500861e-05 | 7.144156098978252e-06 | 28.68% | 40.21% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.4754731562635478e-05 | 8.228466223187545e-06 | 44.23% | 79.31% | 1.79x | ✅ |
| `apply_key_map[single-key]` | 1.779562104981302e-05 | 1.0375187268002613e-05 | 41.70% | 71.52% | 1.72x | ✅ |
| `apply_key_map[two-keys]` | 2.025551119165948e-05 | 1.1903510643696257e-05 | 41.23% | 70.16% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9598006579945845e-05 | 1.1091297448701345e-05 | 43.41% | 76.70% | 1.77x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.557241401841681e-06 | 1.5412092523985348e-06 | 1.03% | 1.04% | 1.01x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1840288826715986e-06 | 1.8877199714857385e-06 | 13.57% | 15.70% | 1.16x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0004098925722657021 | 0.0014096544344514423 | -243.91% | -70.92% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005593016691680466 | 0.0016267669388418864 | -190.86% | -65.62% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00048277980462250347 | 0.0015067091716169068 | -212.09% | -67.96% | 0.32x | ❌ |
