#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.74902319164468e-06 | 8.788354274356136e-06 | -13.41% | -11.83% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.689664782072297e-06 | 8.696293269421415e-06 | -13.09% | -11.58% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.669214049477188e-06 | 8.935314497308065e-06 | -16.51% | -14.17% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 9.605309094698786e-07 | 9.850112470647433e-07 | -2.55% | -2.49% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1444855602659168e-06 | 1.4038781242637524e-06 | -22.66% | -18.48% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.9410498434199025e-06 | 4.901351413219135e-06 | 0.80% | 0.81% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.137885137647576e-06 | 6.138319009680428e-06 | -0.01% | -0.01% | 1.00x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.196470177070464e-06 | 5.475672729492776e-06 | -5.37% | -5.10% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0533099936959447e-05 | 5.223295142140087e-06 | 50.41% | 101.66% | 2.02x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0399948862879563e-05 | 4.665080451762968e-06 | 55.14% | 122.93% | 2.23x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.36626976778963e-06 | 5.818459473326344e-06 | 30.45% | 43.79% | 1.44x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.860454620619175e-06 | 6.1732838038290424e-06 | 30.33% | 43.53% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.426605751058144e-06 | 6.58882284743259e-06 | 30.10% | 43.07% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.844890424319333e-06 | 7.13826816043176e-06 | 27.49% | 37.92% | 1.38x | ✅ |
| `apply_key_map[empty]` | 1.4668442488943321e-05 | 8.172352518670095e-06 | 44.29% | 79.49% | 1.79x | ✅ |
| `apply_key_map[single-key]` | 1.803288543049647e-05 | 1.0652616913660643e-05 | 40.93% | 69.28% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.0491155682789947e-05 | 1.211486436708746e-05 | 40.88% | 69.14% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.957634211676251e-05 | 1.124946295409181e-05 | 42.54% | 74.02% | 1.74x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5616168902250525e-06 | 1.5379417926665333e-06 | 1.52% | 1.54% | 1.02x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.173137880004628e-06 | 1.8973161567498408e-06 | 12.69% | 14.54% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003583831721613494 | 0.0013801927772798177 | -285.12% | -74.03% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000561664203703816 | 0.0016009173747888695 | -185.03% | -64.92% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045352497196280724 | 0.00148925074620011 | -228.37% | -69.55% | 0.30x | ❌ |
