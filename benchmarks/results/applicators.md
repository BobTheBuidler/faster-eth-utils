#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.216673016342755e-06 | 7.801757277080592e-06 | -8.11% | -7.50% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.2339769935544e-06 | 7.859201844410318e-06 | -8.64% | -7.96% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.1246781427465234e-06 | 7.78135507130839e-06 | -9.22% | -8.44% | 0.92x | ❌ |
| `apply_formatter_if[condition-false]` | 8.646405960842253e-07 | 1.0423527183873115e-06 | -20.55% | -17.05% | 0.83x | ❌ |
| `apply_formatter_if[condition-true]` | 1.052104010529952e-06 | 1.4451272850732708e-06 | -37.36% | -27.20% | 0.73x | ❌ |
| `apply_formatter_to_array[empty]` | 4.501019026570977e-06 | 4.629877096160561e-06 | -2.86% | -2.78% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.470599041630561e-06 | 5.94035094953636e-06 | -8.59% | -7.91% | 0.92x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.795603394601834e-06 | 5.010118144228596e-06 | -4.47% | -4.28% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 9.125221985291572e-06 | 5.051596564147744e-06 | 44.64% | 80.64% | 1.81x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.916453025293798e-06 | 4.5650370994353075e-06 | 48.80% | 95.32% | 1.95x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 7.965683405383186e-06 | 5.005383761148414e-06 | 37.16% | 59.14% | 1.59x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.540373898339849e-06 | 5.48357267453614e-06 | 35.79% | 55.74% | 1.56x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.086837093871808e-06 | 6.04454790913823e-06 | 33.48% | 50.33% | 1.50x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.667742311885607e-06 | 6.444230264606861e-06 | 33.34% | 50.02% | 1.50x | ✅ |
| `apply_key_map[empty]` | 1.320704587003137e-05 | 8.126454947541469e-06 | 38.47% | 62.52% | 1.63x | ✅ |
| `apply_key_map[single-key]` | 1.5433774812597985e-05 | 9.683179048274571e-06 | 37.26% | 59.39% | 1.59x | ✅ |
| `apply_key_map[two-keys]` | 1.7517306568230032e-05 | 1.1332665626431232e-05 | 35.31% | 54.57% | 1.55x | ✅ |
| `apply_key_map[unrelated-key]` | 1.651046913236327e-05 | 1.0706582523275556e-05 | 35.15% | 54.21% | 1.54x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.4207193462926978e-06 | 1.4862927571285353e-06 | -4.62% | -4.41% | 0.96x | ❌ |
| `apply_one_of_formatters[second-matches]` | 1.9338119735054908e-06 | 1.82971485137781e-06 | 5.38% | 5.69% | 1.06x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00033874270795576417 | 0.0010363135360828058 | -205.93% | -67.31% | 0.33x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0004872164780287492 | 0.001152651515537272 | -136.58% | -57.73% | 0.42x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0003982568689801412 | 0.0013799138780155838 | -246.49% | -71.14% | 0.29x | ❌ |
