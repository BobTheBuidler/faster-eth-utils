#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.07820999231656e-06 | 9.113452720692097e-06 | -12.82% | -11.36% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.989414728862171e-06 | 9.249615278464787e-06 | -15.77% | -13.62% | 0.86x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.983578092192065e-06 | 9.014016340861256e-06 | -12.91% | -11.43% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.448460928688453e-07 | 9.875545868144998e-07 | -4.52% | -4.32% | 0.96x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1922705195401676e-06 | 1.4145692458873656e-06 | -18.64% | -15.71% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 5.030481795041957e-06 | 5.111822182075447e-06 | -1.62% | -1.59% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.052367477437506e-06 | 6.367625802042236e-06 | -5.21% | -4.95% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.239358096598609e-06 | 5.518738501994404e-06 | -5.33% | -5.06% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0488907977737056e-05 | 5.238723806971097e-06 | 50.05% | 100.22% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.018336950716634e-05 | 4.875307296116523e-06 | 52.12% | 108.88% | 2.09x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.717362824058424e-06 | 5.916067241120017e-06 | 32.13% | 47.35% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.097568722904152e-06 | 6.3507532291039495e-06 | 30.19% | 43.25% | 1.43x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.682685475371999e-06 | 6.7301089620534015e-06 | 30.49% | 43.87% | 1.44x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0221268917558985e-05 | 7.326828354775359e-06 | 28.32% | 39.50% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.5497596884499594e-05 | 8.81254260778962e-06 | 43.14% | 75.86% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.807557882600071e-05 | 1.0998482386815495e-05 | 39.15% | 64.35% | 1.64x | ✅ |
| `apply_key_map[two-keys]` | 2.0428280327187165e-05 | 1.2638802408619057e-05 | 38.13% | 61.63% | 1.62x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9084008627884068e-05 | 1.1986593940045793e-05 | 37.19% | 59.21% | 1.59x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5951447922603477e-06 | 1.5040424947972e-06 | 5.71% | 6.06% | 1.06x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.210882966413298e-06 | 1.8438063928626121e-06 | 16.60% | 19.91% | 1.20x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0004006041904452002 | 0.0014906205589661828 | -272.09% | -73.13% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005904900818716703 | 0.0015480766874013104 | -162.17% | -61.86% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000522202334841994 | 0.0014394442861442763 | -175.65% | -63.72% | 0.36x | ❌ |
