#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.532788204646812e-06 | 8.663995383528697e-06 | -15.02% | -13.06% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.590657137051375e-06 | 8.74500600099724e-06 | -15.21% | -13.20% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.629172142599856e-06 | 8.750138776619314e-06 | -14.69% | -12.81% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 9.594593157921075e-07 | 9.864997551674263e-07 | -2.82% | -2.74% | 0.97x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1615689607656565e-06 | 1.392416967874222e-06 | -19.87% | -16.58% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 4.782513848980661e-06 | 5.03179858682469e-06 | -5.21% | -4.95% | 0.95x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.873460491554132e-06 | 6.229333025619047e-06 | -6.06% | -5.71% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.170854732215758e-06 | 5.487944591560883e-06 | -6.13% | -5.78% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0753936488095576e-05 | 5.195734434157711e-06 | 51.69% | 106.98% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0958835629932062e-05 | 4.673111463794099e-06 | 57.36% | 134.51% | 2.35x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.473169215240427e-06 | 5.844925765742678e-06 | 31.02% | 44.97% | 1.45x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.889508175559859e-06 | 6.176230883574471e-06 | 30.52% | 43.93% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.773135019242954e-06 | 6.652375146630176e-06 | 31.93% | 46.91% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.92580892057331e-06 | 7.0653549756076775e-06 | 28.82% | 40.49% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.4554482529506879e-05 | 8.28150651327685e-06 | 43.10% | 75.75% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.7891081232520092e-05 | 1.0487833177418811e-05 | 41.38% | 70.59% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 2.0310151556970516e-05 | 1.2051759786376465e-05 | 40.66% | 68.52% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9392238729315786e-05 | 1.1247143198668678e-05 | 42.00% | 72.42% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.577821590606254e-06 | 1.5748366642855894e-06 | 0.19% | 0.19% | 1.00x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1929843765521305e-06 | 1.926261886114953e-06 | 12.16% | 13.85% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038146729487163164 | 0.0015111301571423042 | -296.14% | -74.76% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005616514771243607 | 0.0017820836486924342 | -217.29% | -68.48% | 0.32x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004586197491369155 | 0.0014998973451036983 | -227.05% | -69.42% | 0.31x | ❌ |
