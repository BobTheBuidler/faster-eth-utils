#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.844644902978667e-06 | 8.859950229066005e-06 | -12.94% | -11.46% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.812267711909528e-06 | 8.8250416845508e-06 | -12.96% | -11.48% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.986589657218453e-06 | 8.772420472226617e-06 | -9.84% | -8.96% | 0.91x | ❌ |
| `apply_formatter_if[condition-false]` | 9.454116640104418e-07 | 1.0059058150254641e-06 | -6.40% | -6.01% | 0.94x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1893103505816008e-06 | 1.4603195062038013e-06 | -22.79% | -18.56% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 4.855902118989003e-06 | 5.175282162146544e-06 | -6.58% | -6.17% | 0.94x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.9999051767016246e-06 | 6.449677837709716e-06 | -7.50% | -6.97% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.440355744129931e-06 | 5.804328005109218e-06 | -6.69% | -6.27% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.051606538494952e-05 | 5.302442942572949e-06 | 49.58% | 98.32% | 1.98x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0015593423867523e-05 | 4.753394485681887e-06 | 52.54% | 110.70% | 2.11x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.430238073369023e-06 | 5.675402334298644e-06 | 32.68% | 48.54% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.88581895452499e-06 | 6.178054679689836e-06 | 30.47% | 43.83% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.615162408779037e-06 | 6.45044207430559e-06 | 32.91% | 49.06% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.980603267066812e-06 | 6.937709024038832e-06 | 30.49% | 43.86% | 1.44x | ✅ |
| `apply_key_map[empty]` | 1.4931608745441796e-05 | 8.517363076079247e-06 | 42.96% | 75.31% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.7542240946435054e-05 | 1.0150547694559599e-05 | 42.14% | 72.82% | 1.73x | ✅ |
| `apply_key_map[two-keys]` | 1.9470168918019788e-05 | 1.155526738052527e-05 | 40.65% | 68.50% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8703796715627076e-05 | 1.0677513590134622e-05 | 42.91% | 75.17% | 1.75x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7109651892117219e-06 | 1.5254122128273507e-06 | 10.84% | 12.16% | 1.12x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1775752752918476e-06 | 1.8966532579134555e-06 | 12.90% | 14.81% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003642442278408154 | 0.001450400677578613 | -298.19% | -74.89% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000567834823925903 | 0.001650669923078609 | -190.70% | -65.60% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046881326415064087 | 0.0017979678939132496 | -283.51% | -73.93% | 0.26x | ❌ |
