#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.935674412141807e-06 | 8.529627379055048e-06 | -7.48% | -6.96% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.08146016207698e-06 | 8.517966791499584e-06 | -5.40% | -5.12% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.960717736329395e-06 | 8.477851180167597e-06 | -6.50% | -6.10% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0176187793545716e-06 | 9.861193048264891e-07 | 3.10% | 3.19% | 1.03x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2634870561643169e-06 | 1.4480934404916462e-06 | -14.61% | -12.75% | 0.87x | ❌ |
| `apply_formatter_to_array[empty]` | 4.965465111724904e-06 | 4.776092751653216e-06 | 3.81% | 3.97% | 1.04x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.157183345037843e-06 | 6.248695997575152e-06 | -1.49% | -1.46% | 0.99x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.355586520691609e-06 | 5.394382094914362e-06 | -0.72% | -0.72% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0447302468747355e-05 | 5.0350346653854685e-06 | 51.81% | 107.49% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0010195180721075e-05 | 4.606181687507703e-06 | 53.99% | 117.32% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.849851588215656e-06 | 5.589395508397107e-06 | 36.84% | 58.33% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.197054406831703e-06 | 6.001380332237702e-06 | 34.75% | 53.25% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.789859638104841e-06 | 6.466895291628497e-06 | 33.94% | 51.38% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0165376970490764e-05 | 7.0802550674293665e-06 | 30.35% | 43.57% | 1.44x | ✅ |
| `apply_key_map[empty]` | 1.4555219423598581e-05 | 8.59731996009004e-06 | 40.93% | 69.30% | 1.69x | ✅ |
| `apply_key_map[single-key]` | 1.7240054492573357e-05 | 9.915546564908922e-06 | 42.49% | 73.87% | 1.74x | ✅ |
| `apply_key_map[two-keys]` | 1.9357947155596203e-05 | 1.1476400282621104e-05 | 40.71% | 68.68% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8225588008798607e-05 | 1.0757372347510752e-05 | 40.98% | 69.42% | 1.69x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7708813638365968e-06 | 1.4954447758110574e-06 | 15.55% | 18.42% | 1.18x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2617050003145074e-06 | 1.9593580970243083e-06 | 13.37% | 15.43% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003644245333743302 | 0.0013247723419443538 | -263.52% | -72.49% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005685873665445136 | 0.001579562794781949 | -177.80% | -64.00% | 0.36x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00047505623004452674 | 0.0015682848925621328 | -230.13% | -69.71% | 0.30x | ❌ |
