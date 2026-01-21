#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.514569636336775e-06 | 8.687480251396138e-06 | -15.61% | -13.50% | 0.86x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.560423345623981e-06 | 8.725636525025361e-06 | -15.41% | -13.35% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.548793384715509e-06 | 8.763393048268966e-06 | -16.09% | -13.86% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 9.747446909083483e-07 | 9.90794518893027e-07 | -1.65% | -1.62% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1629772562025268e-06 | 1.4077436740349887e-06 | -21.05% | -17.39% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.759720400282364e-06 | 4.829810647695464e-06 | -1.47% | -1.45% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.837664436479526e-06 | 6.19443630567358e-06 | -6.11% | -5.76% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.126982863541653e-06 | 5.423824617380416e-06 | -5.79% | -5.47% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0562752552815215e-05 | 5.188571036322225e-06 | 50.88% | 103.58% | 2.04x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.051212239057141e-05 | 4.67822323968662e-06 | 55.50% | 124.70% | 2.25x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.304249749063632e-06 | 5.7415596379596445e-06 | 30.86% | 44.63% | 1.45x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.810735007662051e-06 | 6.0922071214710534e-06 | 30.85% | 44.62% | 1.45x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.266350379950957e-06 | 6.550217630500279e-06 | 29.31% | 41.47% | 1.41x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.804892770102426e-06 | 7.041620931019358e-06 | 28.18% | 39.24% | 1.39x | ✅ |
| `apply_key_map[empty]` | 1.4314424268178233e-05 | 8.26973265081869e-06 | 42.23% | 73.09% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.7577371495741438e-05 | 1.037288750946348e-05 | 40.99% | 69.45% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.0119200605100143e-05 | 1.2011376528018204e-05 | 40.30% | 67.50% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9326749882879825e-05 | 1.115109971354388e-05 | 42.30% | 73.32% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.666169134969945e-06 | 1.589762966835015e-06 | 4.59% | 4.81% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.160833998801921e-06 | 1.9406879552643873e-06 | 10.19% | 11.34% | 1.11x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036541205156572464 | 0.001442221692429161 | -294.68% | -74.66% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005629087149879829 | 0.0016358789037513959 | -190.61% | -65.59% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004595727365650338 | 0.0017343503389258136 | -277.38% | -73.50% | 0.26x | ❌ |
