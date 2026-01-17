#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.546115409868979e-06 | 8.581692682799521e-06 | -13.72% | -12.07% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.579811648019744e-06 | 8.7871316948022e-06 | -15.93% | -13.74% | 0.86x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.566666503123241e-06 | 8.850332259326614e-06 | -16.96% | -14.50% | 0.85x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0033301146616182e-06 | 9.68681248302782e-07 | 3.45% | 3.58% | 1.04x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1866014329782438e-06 | 1.4165581881715558e-06 | -19.38% | -16.23% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.890718967937254e-06 | 4.982886853930246e-06 | -1.88% | -1.85% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.987580743371402e-06 | 6.236624912881434e-06 | -4.16% | -3.99% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.304495627687643e-06 | 5.521961879828091e-06 | -4.10% | -3.94% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0566337860538808e-05 | 5.309166877290424e-06 | 49.75% | 99.02% | 1.99x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0755456927909417e-05 | 4.755695232013985e-06 | 55.78% | 126.16% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.352794889874985e-06 | 6.046359126875046e-06 | 27.61% | 38.15% | 1.38x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.898182834396039e-06 | 6.2039628925607696e-06 | 30.28% | 43.43% | 1.43x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.437041590250283e-06 | 6.6947257739803515e-06 | 29.06% | 40.96% | 1.41x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.831622948842878e-06 | 7.15544692801643e-06 | 27.22% | 37.40% | 1.37x | ✅ |
| `apply_key_map[empty]` | 1.4806460765290861e-05 | 8.332775592338837e-06 | 43.72% | 77.69% | 1.78x | ✅ |
| `apply_key_map[single-key]` | 1.8068859524812524e-05 | 1.063970774280501e-05 | 41.12% | 69.82% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 2.0617149142848905e-05 | 1.1888408470729353e-05 | 42.34% | 73.42% | 1.73x | ✅ |
| `apply_key_map[unrelated-key]` | 1.955041628139517e-05 | 1.1389966962177488e-05 | 41.74% | 71.65% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6070329037182658e-06 | 1.5942757130946788e-06 | 0.79% | 0.80% | 1.01x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.225622383203118e-06 | 1.980438790769294e-06 | 11.02% | 12.38% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003781312829977145 | 0.0013490026624409942 | -256.76% | -71.97% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005564071075208617 | 0.001579297496023889 | -183.84% | -64.77% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046067952171450317 | 0.0016487157821323951 | -257.89% | -72.06% | 0.28x | ❌ |
