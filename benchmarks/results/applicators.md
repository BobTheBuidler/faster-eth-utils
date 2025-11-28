#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.826092068493713e-06 | 8.594359366613391e-06 | -9.82% | -8.94% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.913124213989177e-06 | 8.569441364306926e-06 | -8.29% | -7.66% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.947923425162521e-06 | 8.536939207790073e-06 | -7.41% | -6.90% | 0.93x | ❌ |
| `apply_formatter_if[condition-false]` | 9.832132877611468e-07 | 9.75374979607588e-07 | 0.80% | 0.80% | 1.01x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2155750570703602e-06 | 1.4428238074923117e-06 | -18.69% | -15.75% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.9827160912536065e-06 | 4.605508499074293e-06 | 7.57% | 8.19% | 1.08x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.196041256830175e-06 | 6.127268589155531e-06 | 1.11% | 1.12% | 1.01x | ✅ |
| `apply_formatter_to_array[single-item]` | 5.355001629413421e-06 | 5.356470871864373e-06 | -0.03% | -0.03% | 1.00x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0274654064145484e-05 | 4.9593860020350106e-06 | 51.73% | 107.18% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.850914127683487e-06 | 4.358030993176148e-06 | 55.76% | 126.04% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.677658407944425e-06 | 5.548204068151599e-06 | 36.06% | 56.40% | 1.56x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.094859876876587e-06 | 5.945930140713209e-06 | 34.62% | 52.96% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.62848886759416e-06 | 6.432036342006595e-06 | 33.20% | 49.70% | 1.50x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0030586710609665e-05 | 6.777400234383739e-06 | 32.43% | 48.00% | 1.48x | ✅ |
| `apply_key_map[empty]` | 1.5028794993058642e-05 | 8.443335706558979e-06 | 43.82% | 78.00% | 1.78x | ✅ |
| `apply_key_map[single-key]` | 1.757159397171734e-05 | 1.0274344795702254e-05 | 41.53% | 71.02% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9694298055228032e-05 | 1.1858221821630841e-05 | 39.79% | 66.08% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8458635449057643e-05 | 1.0871891319325684e-05 | 41.10% | 69.78% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6539355195733157e-06 | 1.485526424161781e-06 | 10.18% | 11.34% | 1.11x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2288483374389863e-06 | 1.8383329229106083e-06 | 17.52% | 21.24% | 1.21x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038272627369616725 | 0.0013435467583465814 | -251.05% | -71.51% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005944687505425239 | 0.0015806179513333518 | -165.89% | -62.39% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004907045395506834 | 0.0013883330669853383 | -182.93% | -64.66% | 0.35x | ❌ |
