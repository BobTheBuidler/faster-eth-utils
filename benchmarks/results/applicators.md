#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.606643498158763e-06 | 8.954132166761364e-06 | -17.71% | -15.05% | 0.85x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.643805183645088e-06 | 8.955500369917739e-06 | -17.16% | -14.65% | 0.85x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.62422356970251e-06 | 8.700967298669304e-06 | -14.12% | -12.37% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.92557803816097e-07 | 1.068628163158905e-06 | -7.66% | -7.12% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1883173463572568e-06 | 1.5118330357301644e-06 | -27.22% | -21.40% | 0.79x | ❌ |
| `apply_formatter_to_array[empty]` | 4.697279753916984e-06 | 4.774631593606426e-06 | -1.65% | -1.62% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.845047943780471e-06 | 6.0185134788310495e-06 | -2.97% | -2.88% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.136189900648043e-06 | 5.3212222983431265e-06 | -3.60% | -3.48% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.056231502094265e-05 | 5.281616174171504e-06 | 50.00% | 99.98% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0703569581923733e-05 | 4.7558876523744675e-06 | 55.57% | 125.06% | 2.25x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.350836504823168e-06 | 5.613946222928702e-06 | 32.77% | 48.75% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.10521011253299e-06 | 5.923370893716978e-06 | 34.95% | 53.72% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.487453642143851e-06 | 6.328339953337886e-06 | 33.30% | 49.92% | 1.50x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.905458580964107e-06 | 6.832563101443909e-06 | 31.02% | 44.97% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.4592767888546638e-05 | 8.127758081297526e-06 | 44.30% | 79.54% | 1.80x | ✅ |
| `apply_key_map[single-key]` | 1.78686826159724e-05 | 1.0262078281733618e-05 | 42.57% | 74.12% | 1.74x | ✅ |
| `apply_key_map[two-keys]` | 2.052468467525702e-05 | 1.2068307498398853e-05 | 41.20% | 70.07% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9435279824886897e-05 | 1.0939076848764517e-05 | 43.72% | 77.67% | 1.78x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5432401278615357e-06 | 1.4778031200244186e-06 | 4.24% | 4.43% | 1.04x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.103829314617294e-06 | 1.8054894411725678e-06 | 14.18% | 16.52% | 1.17x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003637598253968514 | 0.0014217779879704482 | -290.86% | -74.42% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005558294396072802 | 0.0016070083775997772 | -189.12% | -65.41% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004551297933494884 | 0.0016895862708332142 | -271.23% | -73.06% | 0.27x | ❌ |
