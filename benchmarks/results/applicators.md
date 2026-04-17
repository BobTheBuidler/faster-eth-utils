#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.846405510187804e-06 | 9.315910664141316e-06 | -18.73% | -15.77% | 0.84x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.19550686753613e-06 | 8.923080933822343e-06 | -8.88% | -8.15% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.944649788029976e-06 | 9.212829593032993e-06 | -15.96% | -13.77% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 9.86587486359891e-07 | 1.053420890992795e-06 | -6.77% | -6.34% | 0.94x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2215365980635447e-06 | 1.528855051856028e-06 | -25.16% | -20.10% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 5.456148234250133e-06 | 5.316758845919438e-06 | 2.55% | 2.62% | 1.03x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.2433963373752745e-06 | 6.480522448447714e-06 | -3.80% | -3.66% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.451765632065073e-06 | 6.03703073258043e-06 | -10.74% | -9.69% | 0.90x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0499032491354917e-05 | 5.502598374559533e-06 | 47.59% | 90.80% | 1.91x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0200738896944197e-05 | 4.9145536764042435e-06 | 51.82% | 107.56% | 2.08x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.901047700326204e-06 | 5.634528853758471e-06 | 36.70% | 57.97% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.382623156084223e-06 | 6.2475454892118515e-06 | 33.41% | 50.18% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.693581003218679e-06 | 6.6266958005419e-06 | 31.64% | 46.28% | 1.46x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0121121895963328e-05 | 7.364429354111611e-06 | 27.24% | 37.43% | 1.37x | ✅ |
| `apply_key_map[empty]` | 1.5306571087129032e-05 | 8.690152248442321e-06 | 43.23% | 76.14% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.844676631409362e-05 | 1.059325228695728e-05 | 42.57% | 74.14% | 1.74x | ✅ |
| `apply_key_map[two-keys]` | 2.04249892808521e-05 | 1.2327735659508131e-05 | 39.64% | 65.68% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9827490179437664e-05 | 1.1403279453361418e-05 | 42.49% | 73.88% | 1.74x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.8212448707434624e-06 | 1.6152877952555781e-06 | 11.31% | 12.75% | 1.13x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2614224186703803e-06 | 1.996262652598233e-06 | 11.73% | 13.28% | 1.13x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00039812820433773074 | 0.0015898146945395608 | -299.32% | -74.96% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005983544158978202 | 0.0020030574931264636 | -234.76% | -70.13% | 0.30x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004839496216766595 | 0.001636897823117891 | -238.24% | -70.43% | 0.30x | ❌ |
