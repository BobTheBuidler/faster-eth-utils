#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.888789896028914e-06 | 8.997147888500495e-06 | -14.05% | -12.32% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.875127881187881e-06 | 9.047824588880623e-06 | -14.89% | -12.96% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.842571892410189e-06 | 9.164938083224467e-06 | -16.86% | -14.43% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 9.499310831804884e-07 | 1.0018975716132814e-06 | -5.47% | -5.19% | 0.95x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1455582664873426e-06 | 1.4157202563184484e-06 | -23.58% | -19.08% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 5.135772142501701e-06 | 5.143980696621016e-06 | -0.16% | -0.16% | 1.00x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.155552871121471e-06 | 6.519119197186341e-06 | -5.91% | -5.58% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.403548860081809e-06 | 5.6217375516924006e-06 | -4.04% | -3.88% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0602156246167816e-05 | 5.057190003241465e-06 | 52.30% | 109.65% | 2.10x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0182478136518934e-05 | 4.561446735258472e-06 | 55.20% | 123.23% | 2.23x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.765716827374624e-06 | 5.670762916542418e-06 | 35.31% | 54.58% | 1.55x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.222958594383188e-06 | 6.07925388517983e-06 | 34.09% | 51.71% | 1.52x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.881811089724802e-06 | 6.662982300503127e-06 | 32.57% | 48.31% | 1.48x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0418937927906202e-05 | 6.85872488550079e-06 | 34.17% | 51.91% | 1.52x | ✅ |
| `apply_key_map[empty]` | 1.5496127953912055e-05 | 8.964089139511247e-06 | 42.15% | 72.87% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.825018074013698e-05 | 1.1040149678997901e-05 | 39.51% | 65.31% | 1.65x | ✅ |
| `apply_key_map[two-keys]` | 2.088786871558111e-05 | 1.234367460636482e-05 | 40.91% | 69.22% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.923257812126593e-05 | 1.158836723186396e-05 | 39.75% | 65.96% | 1.66x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5478723548312319e-06 | 1.5050558534630264e-06 | 2.77% | 2.84% | 1.03x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1357701309216216e-06 | 1.8794973371651985e-06 | 12.00% | 13.64% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0004167938573311619 | 0.001434825170992175 | -244.25% | -70.95% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006042768503649548 | 0.0016322895223148193 | -170.12% | -62.98% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005467431630301455 | 0.0014522687050691676 | -165.62% | -62.35% | 0.38x | ❌ |
