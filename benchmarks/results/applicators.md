#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.59608812249682e-06 | 8.768493641458639e-06 | -15.43% | -13.37% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.584734768029477e-06 | 8.780352778093292e-06 | -15.76% | -13.62% | 0.86x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.58779204748135e-06 | 8.673196871722583e-06 | -14.30% | -12.51% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 9.49129230100514e-07 | 9.546402451489045e-07 | -0.58% | -0.58% | 0.99x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1369035205437138e-06 | 1.3943771841241742e-06 | -22.65% | -18.47% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.713172359244216e-06 | 4.988642596684831e-06 | -5.84% | -5.52% | 0.94x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.835259981272605e-06 | 6.240490851091052e-06 | -6.94% | -6.49% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.105036825309253e-06 | 5.537926279423221e-06 | -8.48% | -7.82% | 0.92x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0470058517203239e-05 | 5.337770947554033e-06 | 49.02% | 96.15% | 1.96x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0530960880605944e-05 | 4.765912696106473e-06 | 54.74% | 120.96% | 2.21x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.238262292631892e-06 | 5.752079553386657e-06 | 30.18% | 43.22% | 1.43x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.757514141153096e-06 | 6.111256929595569e-06 | 30.22% | 43.30% | 1.43x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.25298374948592e-06 | 6.520609141494741e-06 | 29.53% | 41.90% | 1.42x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.701751864094368e-06 | 6.886403637201973e-06 | 29.02% | 40.88% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.4539336402483377e-05 | 8.354843561906781e-06 | 42.54% | 74.02% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.75444517262677e-05 | 1.0286713463683101e-05 | 41.37% | 70.55% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9945592095977194e-05 | 1.1933177171752017e-05 | 40.17% | 67.14% | 1.67x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9165943905890095e-05 | 1.1106473373122373e-05 | 42.05% | 72.57% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.630740978966377e-06 | 1.4687825858959273e-06 | 9.93% | 11.03% | 1.11x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1639547677588143e-06 | 1.8221631342661754e-06 | 15.79% | 18.76% | 1.19x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036765750333089456 | 0.0014314552788911139 | -289.34% | -74.32% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005540406653838222 | 0.00162446915646207 | -193.20% | -65.89% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045460924041987777 | 0.0017070100892254052 | -275.49% | -73.37% | 0.27x | ❌ |
