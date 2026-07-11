#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.293095582085219e-06 | 8.103805669336586e-06 | -11.12% | -10.00% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.3175901487320375e-06 | 8.224304947287544e-06 | -12.39% | -11.02% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.315256144984189e-06 | 8.300344263717379e-06 | -13.47% | -11.87% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.920886783111783e-07 | 9.674174961946113e-07 | 2.49% | 2.55% | 1.03x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2298309610661055e-06 | 1.4056880915005717e-06 | -14.30% | -12.51% | 0.87x | ❌ |
| `apply_formatter_to_array[empty]` | 4.50759193081135e-06 | 4.5361467630795965e-06 | -0.63% | -0.63% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.6113005887389905e-06 | 5.9279861657161625e-06 | -5.64% | -5.34% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.830143247182412e-06 | 5.128010272075028e-06 | -6.17% | -5.81% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0091821712181986e-05 | 4.65259303910697e-06 | 53.90% | 116.91% | 2.17x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.840919358156761e-06 | 4.20926316199512e-06 | 57.23% | 133.79% | 2.34x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.267576510067392e-06 | 5.0991900715659005e-06 | 38.32% | 62.14% | 1.62x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.66026029673463e-06 | 5.466308673273063e-06 | 36.88% | 58.43% | 1.58x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.18667301224035e-06 | 5.9426396773995475e-06 | 35.31% | 54.59% | 1.55x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.616962022722867e-06 | 6.3715839659756e-06 | 33.75% | 50.94% | 1.51x | ✅ |
| `apply_key_map[empty]` | 1.4639545629803654e-05 | 8.527372221239658e-06 | 41.75% | 71.68% | 1.72x | ✅ |
| `apply_key_map[single-key]` | 1.7043443242551538e-05 | 9.926629313314026e-06 | 41.76% | 71.69% | 1.72x | ✅ |
| `apply_key_map[two-keys]` | 1.9069550099636195e-05 | 1.1476772057021768e-05 | 39.82% | 66.16% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8282871927744204e-05 | 1.1056705558145356e-05 | 39.52% | 65.36% | 1.65x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5293493882121876e-06 | 1.459129831222462e-06 | 4.59% | 4.81% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.0174441275504533e-06 | 1.8566761147562513e-06 | 7.97% | 8.66% | 1.09x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00030364849783787526 | 0.0009831077795166793 | -223.77% | -69.11% | 0.31x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0004540026000010726 | 0.0013982299939489552 | -207.98% | -67.53% | 0.32x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000365867633486369 | 0.001103131294469249 | -201.51% | -66.83% | 0.33x | ❌ |
