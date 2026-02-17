#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.620975226516034e-06 | 8.725122661563436e-06 | -14.49% | -12.65% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.820427579706174e-06 | 8.766890404294335e-06 | -12.10% | -10.80% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.74027696198119e-06 | 9.069111532348089e-06 | -17.17% | -14.65% | 0.85x | ❌ |
| `apply_formatter_if[condition-false]` | 9.473936712968373e-07 | 1.001728804206882e-06 | -5.74% | -5.42% | 0.95x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1782400984153763e-06 | 1.4287750336170205e-06 | -21.26% | -17.53% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.760951832069554e-06 | 4.9977710361773105e-06 | -4.97% | -4.74% | 0.95x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.831536818458358e-06 | 6.30427797705653e-06 | -8.11% | -7.50% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.180339681356852e-06 | 5.447601012220452e-06 | -5.16% | -4.91% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.027910526100765e-05 | 5.351040122885942e-06 | 47.94% | 92.10% | 1.92x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0407381313077071e-05 | 4.777584868065982e-06 | 54.09% | 117.84% | 2.18x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.293389348381008e-06 | 5.645494877754716e-06 | 31.93% | 46.90% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.782244630494086e-06 | 5.952280694157445e-06 | 32.22% | 47.54% | 1.48x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.317540991964084e-06 | 6.453285051669898e-06 | 30.74% | 44.38% | 1.44x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.671104877110317e-06 | 6.873691190458607e-06 | 28.93% | 40.70% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.4373169307723195e-05 | 8.229792804256979e-06 | 42.74% | 74.65% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.740159162599317e-05 | 1.010303411282212e-05 | 41.94% | 72.24% | 1.72x | ✅ |
| `apply_key_map[two-keys]` | 1.985127452589151e-05 | 1.1997696493707554e-05 | 39.56% | 65.46% | 1.65x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8979576386543304e-05 | 1.0746129603001643e-05 | 43.38% | 76.62% | 1.77x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5428184933466581e-06 | 1.4573591785475248e-06 | 5.54% | 5.86% | 1.06x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.156795103392697e-06 | 1.7919489946209059e-06 | 16.92% | 20.36% | 1.20x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003620369440918591 | 0.0014669990820429988 | -305.21% | -75.32% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005510315190039694 | 0.0016919533083633103 | -207.05% | -67.43% | 0.33x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045169597086752256 | 0.0017927958932382612 | -296.90% | -74.80% | 0.25x | ❌ |
