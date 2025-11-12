#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.920867552330283e-06 | 8.268354100503774e-06 | -4.39% | -4.20% | 0.96x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.742961409717328e-06 | 8.422994393627809e-06 | -8.78% | -8.07% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.881589247653578e-06 | 8.253475665782997e-06 | -4.72% | -4.51% | 0.95x | ❌ |
| `apply_formatter_if[condition-false]` | 9.986491415982752e-07 | 9.821600232375123e-07 | 1.65% | 1.68% | 1.02x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1925058262919572e-06 | 1.4163871562591246e-06 | -18.77% | -15.81% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.893834820383733e-06 | 4.744416765907536e-06 | 3.05% | 3.15% | 1.03x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.106824774702131e-06 | 6.2267520565238475e-06 | -1.96% | -1.93% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.329852799526126e-06 | 5.395971362632387e-06 | -1.24% | -1.23% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0779731827345829e-05 | 5.078838457112658e-06 | 52.89% | 112.25% | 2.12x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0204933097190517e-05 | 4.599237618013128e-06 | 54.93% | 121.88% | 2.22x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.459147806347361e-06 | 5.646227708275582e-06 | 33.25% | 49.82% | 1.50x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.96370078492256e-06 | 5.989008187941294e-06 | 33.19% | 49.67% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.553806252694541e-06 | 6.405951264684159e-06 | 32.95% | 49.14% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.805428460431292e-06 | 6.866472561719756e-06 | 29.97% | 42.80% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.5204372662525263e-05 | 8.5527815719938e-06 | 43.75% | 77.77% | 1.78x | ✅ |
| `apply_key_map[single-key]` | 1.708137542427628e-05 | 1.0044820670054212e-05 | 41.19% | 70.05% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 1.9566356100841894e-05 | 1.15432528744825e-05 | 41.00% | 69.50% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8576804020390477e-05 | 1.0831905733557006e-05 | 41.69% | 71.50% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7024324423771348e-06 | 1.4719180062044682e-06 | 13.54% | 15.66% | 1.16x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.308324397111575e-06 | 1.851639601663099e-06 | 19.78% | 24.66% | 1.25x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037927974500577593 | 0.0013744479574464752 | -262.38% | -72.40% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005990728104754619 | 0.0016295139135593217 | -172.01% | -63.24% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004924317517199275 | 0.0014341439866889221 | -191.24% | -65.66% | 0.34x | ❌ |
