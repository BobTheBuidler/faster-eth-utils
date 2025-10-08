#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.134835816591504e-06 | 8.566590979274192e-06 | -5.31% | -5.04% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.024778044430473e-06 | 8.548808590911328e-06 | -6.53% | -6.13% | 0.94x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.084442935667933e-06 | 8.539958963718913e-06 | -5.63% | -5.33% | 0.95x | ❌ |
| `apply_formatter_if[condition-false]` | 9.823232574082276e-07 | 1.0293113567880722e-06 | -4.78% | -4.57% | 0.95x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2570172715032105e-06 | 1.4387638646879353e-06 | -14.46% | -12.63% | 0.87x | ❌ |
| `apply_formatter_to_array[empty]` | 5.144206531210607e-06 | 4.7425376068300315e-06 | 7.81% | 8.47% | 1.08x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.258147264366307e-06 | 6.211376667728597e-06 | 0.75% | 0.75% | 1.01x | ✅ |
| `apply_formatter_to_array[single-item]` | 5.4797215093584705e-06 | 5.402224408679621e-06 | 1.41% | 1.43% | 1.01x | ✅ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0315811622833974e-05 | 1.2254583361476665e-05 | -18.79% | -15.82% | 0.84x | ❌ |
| `apply_formatters_to_dict[key-not-present]` | 9.735540410955845e-06 | 1.1734895160616808e-05 | -20.54% | -17.04% | 0.83x | ❌ |
| `apply_formatters_to_sequence[1-item]` | 8.57805776612048e-06 | 5.614261773113275e-06 | 34.55% | 52.79% | 1.53x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.979559862590827e-06 | 6.016931684006618e-06 | 32.99% | 49.24% | 1.49x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.52147555661867e-06 | 6.456017839521368e-06 | 32.20% | 47.48% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.834120887099531e-06 | 6.863850295338753e-06 | 30.20% | 43.27% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.4804647614451589e-05 | 1.1686195160973173e-05 | 21.06% | 26.68% | 1.27x | ✅ |
| `apply_key_map[single-key]` | 1.7158696904223688e-05 | 1.4246188055481134e-05 | 16.97% | 20.44% | 1.20x | ✅ |
| `apply_key_map[two-keys]` | 1.941756249522642e-05 | 1.637516196167889e-05 | 15.67% | 18.58% | 1.19x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8283207971259596e-05 | 1.5168558795405614e-05 | 17.04% | 20.53% | 1.21x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6589398942920826e-06 | 1.5019252876219804e-06 | 9.46% | 10.45% | 1.10x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2179305829062102e-06 | 1.828304051226894e-06 | 17.57% | 21.31% | 1.21x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003700901686120917 | 0.0013142615888891813 | -255.12% | -71.84% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005829067457499967 | 0.0016034126371233966 | -175.07% | -63.65% | 0.36x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00048044165076434645 | 0.0015584918625003346 | -224.39% | -69.17% | 0.31x | ❌ |
