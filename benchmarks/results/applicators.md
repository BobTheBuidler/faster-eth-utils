#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.990907552077592e-06 | 9.188180649434885e-06 | -14.98% | -13.03% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.123409539814762e-06 | 9.028754226818508e-06 | -11.14% | -10.03% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.209736606050165e-06 | 8.909865175608326e-06 | -8.53% | -7.86% | 0.92x | ❌ |
| `apply_formatter_if[condition-false]` | 9.60540357537686e-07 | 1.0366665968228812e-06 | -7.93% | -7.34% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1956176856884213e-06 | 1.458203802514007e-06 | -21.96% | -18.01% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.988409766142549e-06 | 4.9565326315070816e-06 | 0.64% | 0.64% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.20515290463981e-06 | 6.42153682973367e-06 | -3.49% | -3.37% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.38080201280724e-06 | 5.631176034370941e-06 | -4.65% | -4.45% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0750079878914612e-05 | 5.1675158816380525e-06 | 51.93% | 108.03% | 2.08x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0430381932734498e-05 | 4.628925917741358e-06 | 55.62% | 125.33% | 2.25x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.793423923362531e-06 | 5.6556904229418355e-06 | 35.68% | 55.48% | 1.55x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.357005114866535e-06 | 6.121164870929992e-06 | 34.58% | 52.86% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.936423640859768e-06 | 6.553219492733285e-06 | 34.05% | 51.63% | 1.52x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0155442385607917e-05 | 6.989116051982685e-06 | 31.18% | 45.30% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.5502525438651297e-05 | 8.759956909927213e-06 | 43.49% | 76.97% | 1.77x | ✅ |
| `apply_key_map[single-key]` | 1.7990894114230133e-05 | 1.0635856048609732e-05 | 40.88% | 69.15% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.015667832128639e-05 | 1.2111349680081545e-05 | 39.91% | 66.43% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9264674614087832e-05 | 1.1451795897019581e-05 | 40.56% | 68.22% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.571267188798538e-06 | 1.5085600434219582e-06 | 3.99% | 4.16% | 1.04x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.0816596162306525e-06 | 1.859095651807012e-06 | 10.69% | 11.97% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.000392702250741087 | 0.0014834617615266132 | -277.76% | -73.53% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005860800551625734 | 0.0015907363603895473 | -171.42% | -63.16% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00047897257339735513 | 0.0014646926102477806 | -205.80% | -67.30% | 0.33x | ❌ |
