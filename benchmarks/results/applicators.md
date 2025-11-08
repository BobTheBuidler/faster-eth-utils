#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.741965513235844e-06 | 8.54169581504105e-06 | -10.33% | -9.36% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.84438927569057e-06 | 8.556465078925926e-06 | -9.08% | -8.32% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.93953975475825e-06 | 8.517832811653075e-06 | -7.28% | -6.79% | 0.93x | ❌ |
| `apply_formatter_if[condition-false]` | 9.899925901840925e-07 | 9.717723027486508e-07 | 1.84% | 1.87% | 1.02x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2507434851884346e-06 | 1.4035745444378404e-06 | -12.22% | -10.89% | 0.89x | ❌ |
| `apply_formatter_to_array[empty]` | 4.99892736919429e-06 | 4.763222062183552e-06 | 4.72% | 4.95% | 1.05x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.117824201104222e-06 | 6.27241123062234e-06 | -2.53% | -2.46% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.409314437566993e-06 | 5.4531823901056254e-06 | -0.81% | -0.80% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0227119054915402e-05 | 4.947664037804676e-06 | 51.62% | 106.71% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0332975647910576e-05 | 4.360640370372823e-06 | 57.80% | 136.96% | 2.37x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.661176561170255e-06 | 5.530002432999944e-06 | 36.15% | 56.62% | 1.57x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.118559506282933e-06 | 5.993447424655625e-06 | 34.27% | 52.14% | 1.52x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 1.0081133775407192e-05 | 6.658786410133101e-06 | 33.95% | 51.40% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0014883008500997e-05 | 6.795946224068677e-06 | 32.14% | 47.37% | 1.47x | ✅ |
| `apply_key_map[empty]` | 1.4672178225371974e-05 | 8.917752852985808e-06 | 39.22% | 64.53% | 1.65x | ✅ |
| `apply_key_map[single-key]` | 1.7143735747596933e-05 | 1.0619834903596409e-05 | 38.05% | 61.43% | 1.61x | ✅ |
| `apply_key_map[two-keys]` | 1.9546784352813814e-05 | 1.2166622441498151e-05 | 37.76% | 60.66% | 1.61x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8325402638178808e-05 | 1.1228847892769437e-05 | 38.73% | 63.20% | 1.63x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6883978845248468e-06 | 1.4693143531404183e-06 | 12.98% | 14.91% | 1.15x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.268884592698484e-06 | 1.8476343425199465e-06 | 18.57% | 22.80% | 1.23x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037470748451670866 | 0.0013410978706771064 | -257.91% | -72.06% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005910140919853603 | 0.0015172132553949627 | -156.71% | -61.05% | 0.39x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004847588019576373 | 0.0014045177315637734 | -189.74% | -65.49% | 0.35x | ❌ |
