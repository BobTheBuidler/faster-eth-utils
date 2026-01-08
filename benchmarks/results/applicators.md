#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.644313965777821e-06 | 8.59567521288384e-06 | -12.45% | -11.07% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.663004559793863e-06 | 8.570885640073376e-06 | -11.85% | -10.59% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.67095601897935e-06 | 8.497745662571968e-06 | -10.78% | -9.73% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.92459581676981e-07 | 1.070621324527076e-06 | -7.88% | -7.30% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2046744534893943e-06 | 1.5088542515372192e-06 | -25.25% | -20.16% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 4.810955976615151e-06 | 4.960273355952882e-06 | -3.10% | -3.01% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.932107707408804e-06 | 6.492250922110126e-06 | -9.44% | -8.63% | 0.91x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.1757949605371375e-06 | 5.4549727439175995e-06 | -5.39% | -5.12% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.043133378484566e-05 | 5.211276871907326e-06 | 50.04% | 100.17% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0481698151883905e-05 | 4.688299812132876e-06 | 55.27% | 123.57% | 2.24x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.415498472315333e-06 | 5.7085785632079925e-06 | 32.17% | 47.42% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.901672169162173e-06 | 5.98216432927576e-06 | 32.80% | 48.80% | 1.49x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.455472413078046e-06 | 6.433100666342172e-06 | 31.96% | 46.98% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.974644738909979e-06 | 7.1297750926735265e-06 | 28.52% | 39.90% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.4648314618746008e-05 | 8.1789777880934e-06 | 44.16% | 79.10% | 1.79x | ✅ |
| `apply_key_map[single-key]` | 1.8421302330070374e-05 | 1.0355057695469741e-05 | 43.79% | 77.90% | 1.78x | ✅ |
| `apply_key_map[two-keys]` | 1.990088361817106e-05 | 1.1892840372437973e-05 | 40.24% | 67.33% | 1.67x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9340221510098327e-05 | 1.0960185120037719e-05 | 43.33% | 76.46% | 1.76x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7469576030443168e-06 | 1.5905367429070947e-06 | 8.95% | 9.83% | 1.10x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.188657433767195e-06 | 1.921917703548669e-06 | 12.19% | 13.88% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038435491490612 | 0.0014194061383449893 | -269.30% | -72.92% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005552456501675922 | 0.0016151414207920616 | -190.89% | -65.62% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000454757692633118 | 0.0016845138379706086 | -270.42% | -73.00% | 0.27x | ❌ |
