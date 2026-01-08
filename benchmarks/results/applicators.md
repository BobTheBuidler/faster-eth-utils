#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.691151207013546e-06 | 8.428843053626117e-06 | -9.59% | -8.75% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.661341245455592e-06 | 8.532682833273422e-06 | -11.37% | -10.21% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.684535629697157e-06 | 8.613435028910141e-06 | -12.09% | -10.78% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.76368531751479e-07 | 1.063384513700461e-06 | -8.91% | -8.18% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1728044232070304e-06 | 1.455657614915531e-06 | -24.12% | -19.43% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 4.743193822944155e-06 | 4.9143121452010086e-06 | -3.61% | -3.48% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.911112146158576e-06 | 6.1621059728428155e-06 | -4.25% | -4.07% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.1980049825853155e-06 | 5.461947937575242e-06 | -5.08% | -4.83% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0573361553600186e-05 | 5.30049444054116e-06 | 49.87% | 99.48% | 1.99x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0848453941151782e-05 | 4.715108620433339e-06 | 56.54% | 130.08% | 2.30x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.453115670270317e-06 | 5.685146823105143e-06 | 32.74% | 48.69% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.901490246380805e-06 | 5.9935867209520055e-06 | 32.67% | 48.52% | 1.49x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.421072601823362e-06 | 6.415723746506313e-06 | 31.90% | 46.84% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.81523296366932e-06 | 6.880104910558517e-06 | 29.90% | 42.66% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.5513926842015214e-05 | 8.467803579011335e-06 | 45.42% | 83.21% | 1.83x | ✅ |
| `apply_key_map[single-key]` | 1.8705981851527648e-05 | 1.0286487743378009e-05 | 45.01% | 81.85% | 1.82x | ✅ |
| `apply_key_map[two-keys]` | 2.124844876137703e-05 | 1.1748759916044728e-05 | 44.71% | 80.86% | 1.81x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9812625056574814e-05 | 1.1869399369751263e-05 | 40.09% | 66.92% | 1.67x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6942097572264409e-06 | 1.5726033516050127e-06 | 7.18% | 7.73% | 1.08x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.160391684576565e-06 | 1.91070362715125e-06 | 11.56% | 13.07% | 1.13x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003837361935872145 | 0.0014520782061533475 | -278.41% | -73.57% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005774891640917042 | 0.0016452136231154158 | -184.89% | -64.90% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004793004353699979 | 0.001725733882926761 | -260.05% | -72.23% | 0.28x | ❌ |
