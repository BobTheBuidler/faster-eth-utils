#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.154058652441985e-06 | 8.81594425927261e-06 | -8.12% | -7.51% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.072370609109773e-06 | 8.837984343579747e-06 | -9.48% | -8.66% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.113825401801197e-06 | 8.878614117081271e-06 | -9.43% | -8.61% | 0.91x | ❌ |
| `apply_formatter_if[condition-false]` | 9.381591994394562e-07 | 1.0228530499056318e-06 | -9.03% | -8.28% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1746008430501144e-06 | 1.4541016990253084e-06 | -23.80% | -19.22% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 5.0020961102017035e-06 | 4.999062507386358e-06 | 0.06% | 0.06% | 1.00x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.119663324585903e-06 | 6.380947028459435e-06 | -4.27% | -4.09% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.314846651074924e-06 | 5.591280949018465e-06 | -5.20% | -4.94% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.092151517438036e-05 | 5.298310976048906e-06 | 51.49% | 106.13% | 2.06x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.053897186212989e-05 | 4.8596591332889154e-06 | 53.89% | 116.87% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.645262313013473e-06 | 5.676447979226967e-06 | 34.34% | 52.30% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.254785716342459e-06 | 6.091249782749028e-06 | 34.18% | 51.94% | 1.52x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.829958045095567e-06 | 6.854344352931707e-06 | 30.27% | 43.41% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.006303929274731e-05 | 6.880029095758083e-06 | 31.63% | 46.26% | 1.46x | ✅ |
| `apply_key_map[empty]` | 1.5455135751475304e-05 | 8.96763926573842e-06 | 41.98% | 72.34% | 1.72x | ✅ |
| `apply_key_map[single-key]` | 1.8265520870718222e-05 | 1.0942481456824056e-05 | 40.09% | 66.92% | 1.67x | ✅ |
| `apply_key_map[two-keys]` | 2.0029087501545974e-05 | 1.2308481485304775e-05 | 38.55% | 62.73% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9184000261887166e-05 | 1.1707796232194347e-05 | 38.97% | 63.86% | 1.64x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5300631629270328e-06 | 1.4890919598697406e-06 | 2.68% | 2.75% | 1.03x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.108329297133097e-06 | 1.8501026894868927e-06 | 12.25% | 13.96% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00040159744395481953 | 0.0014835086747576397 | -269.40% | -72.93% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006001721219693977 | 0.0016203934390670552 | -169.99% | -62.96% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004835103151231866 | 0.001493454248038524 | -208.88% | -67.62% | 0.32x | ❌ |
