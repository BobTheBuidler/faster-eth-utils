#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 6.6383006611736945e-06 | 7.5604882266096834e-06 | -13.89% | -12.20% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 6.635327752787324e-06 | 7.6236905501948415e-06 | -14.90% | -12.96% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 6.622085529233174e-06 | 7.740133602281336e-06 | -16.88% | -14.44% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 7.662903732350617e-07 | 8.380503498470243e-07 | -9.36% | -8.56% | 0.91x | ❌ |
| `apply_formatter_if[condition-true]` | 9.192034906817434e-07 | 1.2342144241459925e-06 | -34.27% | -25.52% | 0.74x | ❌ |
| `apply_formatter_to_array[empty]` | 4.2338842116235965e-06 | 4.383097579215778e-06 | -3.52% | -3.40% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.082278046220707e-06 | 5.674144986719327e-06 | -11.65% | -10.43% | 0.90x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.494347439952117e-06 | 4.7804172307763235e-06 | -6.37% | -5.98% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 8.651233902731755e-06 | 4.469373309312037e-06 | 48.34% | 93.57% | 1.94x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.312367408768124e-06 | 4.06463635952975e-06 | 51.10% | 104.50% | 2.05x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 7.228341053111601e-06 | 4.805582207125123e-06 | 33.52% | 50.42% | 1.50x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 7.712294594034798e-06 | 5.236211921166652e-06 | 32.11% | 47.29% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 8.160737293508564e-06 | 5.710686533336707e-06 | 30.02% | 42.90% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 8.539361341583962e-06 | 6.024124356867534e-06 | 29.45% | 41.75% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.392536434029133e-05 | 8.384933992375016e-06 | 39.79% | 66.08% | 1.66x | ✅ |
| `apply_key_map[single-key]` | 1.5910659090918756e-05 | 9.743185505179658e-06 | 38.76% | 63.30% | 1.63x | ✅ |
| `apply_key_map[two-keys]` | 1.7758105049552338e-05 | 1.0920536572822677e-05 | 38.50% | 62.61% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.679214763211278e-05 | 1.0342400856454598e-05 | 38.41% | 62.36% | 1.62x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.310561923406855e-06 | 1.2995713085006836e-06 | 0.84% | 0.85% | 1.01x | ✅ |
| `apply_one_of_formatters[second-matches]` | 1.684205534145169e-06 | 1.6051740651137116e-06 | 4.69% | 4.92% | 1.05x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0002527096300177697 | 0.0008095295898616143 | -220.34% | -68.78% | 0.31x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000375569540540578 | 0.0009862907847224792 | -162.61% | -61.92% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00030044937645435125 | 0.0010517507771742598 | -250.06% | -71.43% | 0.29x | ❌ |
