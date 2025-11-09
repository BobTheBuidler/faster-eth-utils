#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.946269249204499e-06 | 8.548344482918555e-06 | -7.58% | -7.04% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.888899681270679e-06 | 8.50356005915335e-06 | -7.79% | -7.23% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.331736340595985e-06 | 8.486959859282275e-06 | -1.86% | -1.83% | 0.98x | ❌ |
| `apply_formatter_if[condition-false]` | 1.005380433769066e-06 | 9.556622511791074e-07 | 4.95% | 5.20% | 1.05x | ✅ |
| `apply_formatter_if[condition-true]` | 1.243254138956788e-06 | 1.3792973639593975e-06 | -10.94% | -9.86% | 0.90x | ❌ |
| `apply_formatter_to_array[empty]` | 4.95057956892789e-06 | 4.808419089953836e-06 | 2.87% | 2.96% | 1.03x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.169189141008101e-06 | 6.31245406055452e-06 | -2.32% | -2.27% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.4283154263468685e-06 | 5.425116703780014e-06 | 0.06% | 0.06% | 1.00x | ✅ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0709020672153161e-05 | 5.008049101071998e-06 | 53.24% | 113.84% | 2.14x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0278260351367412e-05 | 4.506784279597316e-06 | 56.15% | 128.06% | 2.28x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.578436173891044e-06 | 5.611184460448526e-06 | 34.59% | 52.88% | 1.53x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.094316196626609e-06 | 5.964004816297265e-06 | 34.42% | 52.49% | 1.52x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.483232486185985e-06 | 6.43759568887947e-06 | 32.12% | 47.31% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.819760216681493e-06 | 6.882895802029921e-06 | 29.91% | 42.67% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.5336761004537896e-05 | 9.115116321536437e-06 | 40.57% | 68.26% | 1.68x | ✅ |
| `apply_key_map[single-key]` | 1.7156175606649268e-05 | 1.062597724574323e-05 | 38.06% | 61.46% | 1.61x | ✅ |
| `apply_key_map[two-keys]` | 1.9455601036438527e-05 | 1.2095944483946261e-05 | 37.83% | 60.84% | 1.61x | ✅ |
| `apply_key_map[unrelated-key]` | 1.829829185744097e-05 | 1.1241256207852115e-05 | 38.57% | 62.78% | 1.63x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.693794272489553e-06 | 1.445179036663677e-06 | 14.68% | 17.20% | 1.17x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2032654855324455e-06 | 1.8063207899569858e-06 | 18.02% | 21.98% | 1.22x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003679287321430563 | 0.0013647622717553878 | -270.93% | -73.04% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006147635420940237 | 0.001636470242320459 | -166.20% | -62.43% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005065384864178574 | 0.0014270138644065864 | -181.72% | -64.50% | 0.35x | ❌ |
