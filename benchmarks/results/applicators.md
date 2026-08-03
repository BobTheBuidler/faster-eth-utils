#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.018260309239513e-06 | 8.969898813957991e-06 | -11.87% | -10.61% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.999116869746576e-06 | 8.79806035722043e-06 | -9.99% | -9.08% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.999537473164288e-06 | 8.896817699641006e-06 | -11.22% | -10.09% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.455198934811108e-07 | 1.0113962784800729e-06 | -6.97% | -6.51% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.149632541480549e-06 | 1.429078933719826e-06 | -24.31% | -19.55% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 4.923575279041213e-06 | 4.897591405018863e-06 | 0.53% | 0.53% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.113573416665662e-06 | 7.0484466843220645e-06 | -15.29% | -13.26% | 0.87x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.262569040170346e-06 | 5.460722932256303e-06 | -3.77% | -3.63% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0769883996439065e-05 | 5.077855623508532e-06 | 52.85% | 112.10% | 2.12x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0451124050565432e-05 | 4.699303202541079e-06 | 55.04% | 122.40% | 2.22x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.733902635926543e-06 | 5.631623951766795e-06 | 35.52% | 55.09% | 1.55x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.309357227694637e-06 | 5.915712106551714e-06 | 36.45% | 57.37% | 1.57x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.788622174897038e-06 | 6.338205126223925e-06 | 35.25% | 54.44% | 1.54x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0186367058468888e-05 | 6.759909182608119e-06 | 33.64% | 50.69% | 1.51x | ✅ |
| `apply_key_map[empty]` | 1.54246389289735e-05 | 9.093280170010209e-06 | 41.05% | 69.63% | 1.70x | ✅ |
| `apply_key_map[single-key]` | 1.8204203361752728e-05 | 1.0887223354186572e-05 | 40.19% | 67.21% | 1.67x | ✅ |
| `apply_key_map[two-keys]` | 2.0184368800052047e-05 | 1.2348347749314599e-05 | 38.82% | 63.46% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9381246239503664e-05 | 1.171807713037318e-05 | 39.54% | 65.40% | 1.65x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6427955811911539e-06 | 1.5059780256824317e-06 | 8.33% | 9.08% | 1.09x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.0952066728433957e-06 | 1.8326801914752394e-06 | 12.53% | 14.32% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00040178871113843756 | 0.0015146117588992925 | -276.97% | -73.47% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005793856499258321 | 0.0015834256249992304 | -173.29% | -63.41% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00047833651918467306 | 0.0014928398847441752 | -212.09% | -67.96% | 0.32x | ❌ |
