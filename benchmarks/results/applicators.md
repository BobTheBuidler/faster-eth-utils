#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.163682780159424e-06 | 8.73207669406119e-06 | -6.96% | -6.51% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.154501394714544e-06 | 8.777092290534443e-06 | -7.63% | -7.09% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.131316774010384e-06 | 8.602994578306572e-06 | -5.80% | -5.48% | 0.95x | ❌ |
| `apply_formatter_if[condition-false]` | 9.405052207458032e-07 | 1.073663770935239e-06 | -14.16% | -12.40% | 0.88x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1593580513137487e-06 | 1.6312561185327331e-06 | -40.70% | -28.93% | 0.71x | ❌ |
| `apply_formatter_to_array[empty]` | 4.972699374678401e-06 | 5.062981613181468e-06 | -1.82% | -1.78% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.315994459159084e-06 | 6.585511959030706e-06 | -4.27% | -4.09% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.347235169918367e-06 | 5.6387029315675075e-06 | -5.45% | -5.17% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0495296731852631e-05 | 5.52233338285417e-06 | 47.38% | 90.05% | 1.90x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0118050463499568e-05 | 4.7543547511760054e-06 | 53.01% | 112.82% | 2.13x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.655258626718793e-06 | 6.279035947455587e-06 | 27.45% | 37.84% | 1.38x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.21661925370336e-06 | 6.602561263405117e-06 | 28.36% | 39.59% | 1.40x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.654965073695513e-06 | 7.0067556248146275e-06 | 27.43% | 37.80% | 1.38x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0307793395926626e-05 | 7.249503686623858e-06 | 29.67% | 42.19% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4883449882234792e-05 | 7.526260075324267e-06 | 49.43% | 97.75% | 1.98x | ✅ |
| `apply_key_map[single-key]` | 1.742602754324981e-05 | 9.342033498592502e-06 | 46.39% | 86.53% | 1.87x | ✅ |
| `apply_key_map[two-keys]` | 1.9708810379483768e-05 | 1.0815139038996988e-05 | 45.13% | 82.23% | 1.82x | ✅ |
| `apply_key_map[unrelated-key]` | 1.881923424662327e-05 | 1.0150235239387517e-05 | 46.06% | 85.41% | 1.85x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6964192353222825e-06 | 1.736358345383402e-06 | -2.35% | -2.30% | 0.98x | ❌ |
| `apply_one_of_formatters[second-matches]` | 2.2718866232704793e-06 | 2.04746098747985e-06 | 9.88% | 10.96% | 1.11x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00035211300318265773 | 0.0012328748630342447 | -250.14% | -71.44% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005695005048387943 | 0.0014896976366900014 | -161.58% | -61.77% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004602782968257642 | 0.001545245614583024 | -235.72% | -70.21% | 0.30x | ❌ |
