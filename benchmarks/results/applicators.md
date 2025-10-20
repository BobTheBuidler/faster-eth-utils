#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.18251642472648e-06 | 9.08468615912436e-06 | -11.03% | -9.93% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.972415916801524e-06 | 9.0614295585476e-06 | -13.66% | -12.02% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.947232835348187e-06 | 9.0536923493713e-06 | -13.92% | -12.22% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.522425971113273e-07 | 1.0495832441622634e-06 | -10.22% | -9.27% | 0.91x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1551304046105508e-06 | 1.4948023630717654e-06 | -29.41% | -22.72% | 0.77x | ❌ |
| `apply_formatter_to_array[empty]` | 5.156140473304204e-06 | 5.2570897674082875e-06 | -1.96% | -1.92% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.326647585186835e-06 | 6.544886120404008e-06 | -3.45% | -3.33% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.528291195517781e-06 | 5.832667249150219e-06 | -5.51% | -5.22% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0669545073346873e-05 | 5.579106568880055e-06 | 47.71% | 91.24% | 1.91x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0203676044293292e-05 | 4.953907824057313e-06 | 51.45% | 105.97% | 2.06x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.742914513414263e-06 | 5.997063303135585e-06 | 31.41% | 45.79% | 1.46x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.489853816303546e-06 | 6.2773960671212795e-06 | 33.85% | 51.18% | 1.51x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.802262592954693e-06 | 6.7535193358399875e-06 | 31.10% | 45.14% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0183534791596485e-05 | 7.154470669127472e-06 | 29.74% | 42.34% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.499629290875755e-05 | 8.934272190734212e-06 | 40.42% | 67.85% | 1.68x | ✅ |
| `apply_key_map[single-key]` | 1.7986919629696613e-05 | 1.0903606490607383e-05 | 39.38% | 64.96% | 1.65x | ✅ |
| `apply_key_map[two-keys]` | 1.9824113398366867e-05 | 1.260158436080961e-05 | 36.43% | 57.31% | 1.57x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8864434729767207e-05 | 1.1678364296496266e-05 | 38.09% | 61.53% | 1.62x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.746434405706495e-06 | 1.6288785795158783e-06 | 6.73% | 7.22% | 1.07x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1906825986708008e-06 | 2.004826835418175e-06 | 8.48% | 9.27% | 1.09x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003473723029795313 | 0.0012428083059438557 | -257.77% | -72.05% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006308328333338742 | 0.0015007951669565995 | -137.91% | -57.97% | 0.42x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005019174486961094 | 0.0013820473132775874 | -175.35% | -63.68% | 0.36x | ❌ |
