#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.720359342668012e-06 | 8.527134928175674e-06 | -10.45% | -9.46% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.73193505757523e-06 | 8.546359706449525e-06 | -10.53% | -9.53% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.731490126874663e-06 | 8.544464232857207e-06 | -10.52% | -9.51% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.963604802609707e-07 | 9.715602173282769e-07 | 2.49% | 2.55% | 1.03x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2120589317920618e-06 | 1.447813761398099e-06 | -19.45% | -16.28% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.903142400170244e-06 | 5.025077240510514e-06 | -2.49% | -2.43% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.0876279477706575e-06 | 6.5230151227432355e-06 | -7.15% | -6.67% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.27437988052197e-06 | 5.67283412044937e-06 | -7.55% | -7.02% | 0.93x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0130992377323027e-05 | 5.1997688971436355e-06 | 48.67% | 94.84% | 1.95x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.703072567659811e-06 | 4.424291306244472e-06 | 54.40% | 119.31% | 2.19x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.80714477803104e-06 | 5.489306424466362e-06 | 37.67% | 60.44% | 1.60x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.26859992893965e-06 | 5.883687553301564e-06 | 36.52% | 57.53% | 1.58x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.708602950704538e-06 | 6.307423528678696e-06 | 35.03% | 53.92% | 1.54x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0078628815539287e-05 | 6.706975264444298e-06 | 33.45% | 50.27% | 1.50x | ✅ |
| `apply_key_map[empty]` | 1.463467028861718e-05 | 6.991790194205202e-06 | 52.22% | 109.31% | 2.09x | ✅ |
| `apply_key_map[single-key]` | 1.673609915233458e-05 | 8.464606520015846e-06 | 49.42% | 97.72% | 1.98x | ✅ |
| `apply_key_map[two-keys]` | 1.8828552126460118e-05 | 1.0113257605843039e-05 | 46.29% | 86.18% | 1.86x | ✅ |
| `apply_key_map[unrelated-key]` | 1.7866629112631525e-05 | 9.24103323007553e-06 | 48.28% | 93.34% | 1.93x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7322970932299998e-06 | 1.5451019708484545e-06 | 10.81% | 12.12% | 1.12x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.3042888261654044e-06 | 1.850274061287756e-06 | 19.70% | 24.54% | 1.25x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003624615904476429 | 0.0012913631178253849 | -256.28% | -71.93% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005791018628330892 | 0.0015446224634950143 | -166.73% | -62.51% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00048679910134238744 | 0.0015060053682584122 | -209.37% | -67.68% | 0.32x | ❌ |
