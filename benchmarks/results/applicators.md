#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.778151680312368e-06 | 8.983433189813312e-06 | -15.50% | -13.42% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.628145260037887e-06 | 8.811694498167092e-06 | -15.52% | -13.43% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.590140744344088e-06 | 8.770272485578059e-06 | -15.55% | -13.46% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 9.659685469568467e-07 | 9.374072887903927e-07 | 2.96% | 3.05% | 1.03x | ✅ |
| `apply_formatter_if[condition-true]` | 1.1441582284914744e-06 | 1.380248795838246e-06 | -20.63% | -17.10% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.818895592669423e-06 | 4.952845886937625e-06 | -2.78% | -2.70% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.951768294851371e-06 | 6.207942921974909e-06 | -4.30% | -4.13% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.425642743501438e-06 | 5.4783937801644885e-06 | -0.97% | -0.96% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.045992300283694e-05 | 5.18655423790722e-06 | 50.41% | 101.67% | 2.02x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0909825129676679e-05 | 4.7369386422639385e-06 | 56.58% | 130.31% | 2.30x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.371457994050845e-06 | 6.035842528582143e-06 | 27.90% | 38.70% | 1.39x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.848619691666753e-06 | 6.3875835005626615e-06 | 27.81% | 38.53% | 1.39x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.36681679945255e-06 | 6.810940373120116e-06 | 27.29% | 37.53% | 1.38x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.826397433537757e-06 | 7.274540249142752e-06 | 25.97% | 35.08% | 1.35x | ✅ |
| `apply_key_map[empty]` | 1.4518431531316335e-05 | 8.422086949260913e-06 | 41.99% | 72.39% | 1.72x | ✅ |
| `apply_key_map[single-key]` | 1.7671009621783392e-05 | 1.0477677199671604e-05 | 40.71% | 68.65% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 2.0565384321171415e-05 | 1.1964748522859309e-05 | 41.82% | 71.88% | 1.72x | ✅ |
| `apply_key_map[unrelated-key]` | 1.904394251586156e-05 | 1.1214129399670605e-05 | 41.11% | 69.82% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6431844884580028e-06 | 1.5400607185429554e-06 | 6.28% | 6.70% | 1.07x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1366438015172754e-06 | 1.9042356602313502e-06 | 10.88% | 12.20% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036619622781579103 | 0.0014346447230048067 | -291.77% | -74.47% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005571664019931175 | 0.0016074622019071948 | -188.51% | -65.34% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045748633231912003 | 0.0017240004511156935 | -276.84% | -73.46% | 0.27x | ❌ |
