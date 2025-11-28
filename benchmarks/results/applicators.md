#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.044536835696146e-06 | 8.483913326194156e-06 | -5.46% | -5.18% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.079813171606304e-06 | 8.355943430833332e-06 | -3.42% | -3.30% | 0.97x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.104683348888123e-06 | 8.320200980941127e-06 | -2.66% | -2.59% | 0.97x | ❌ |
| `apply_formatter_if[condition-false]` | 9.751506539551773e-07 | 1.0202723058361812e-06 | -4.63% | -4.42% | 0.96x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1946068249062585e-06 | 1.4479715151952388e-06 | -21.21% | -17.50% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 5.034820726710255e-06 | 4.690064516401891e-06 | 6.85% | 7.35% | 1.07x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.1556754289242955e-06 | 6.152113205078063e-06 | 0.06% | 0.06% | 1.00x | ✅ |
| `apply_formatter_to_array[single-item]` | 5.517938775506546e-06 | 5.398659505191615e-06 | 2.16% | 2.21% | 1.02x | ✅ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0517333657927016e-05 | 4.907890922972543e-06 | 53.34% | 114.29% | 2.14x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0129871723246956e-05 | 4.370380032009321e-06 | 56.86% | 131.78% | 2.32x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.697244898329988e-06 | 5.5806676428982665e-06 | 35.83% | 55.85% | 1.56x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.114146562108901e-06 | 5.955586137320709e-06 | 34.66% | 53.04% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.630495036888453e-06 | 6.386939139314162e-06 | 33.68% | 50.78% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.854252996654513e-06 | 6.806366535011612e-06 | 30.93% | 44.78% | 1.45x | ✅ |
| `apply_key_map[empty]` | 1.5297663835739504e-05 | 8.527637386781287e-06 | 44.26% | 79.39% | 1.79x | ✅ |
| `apply_key_map[single-key]` | 1.7020534448244805e-05 | 1.0440332860603728e-05 | 38.66% | 63.03% | 1.63x | ✅ |
| `apply_key_map[two-keys]` | 1.9522479338573862e-05 | 1.2006430374792075e-05 | 38.50% | 62.60% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8486975753755327e-05 | 1.1198930567756609e-05 | 39.42% | 65.08% | 1.65x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.633044363914318e-06 | 1.4969943433368234e-06 | 8.33% | 9.09% | 1.09x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.205766590850885e-06 | 1.849409086551667e-06 | 16.16% | 19.27% | 1.19x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003643886390882871 | 0.0013603736324230803 | -273.33% | -73.21% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006153838521077733 | 0.0016192928829596137 | -163.14% | -62.00% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004991614032455652 | 0.0014255109237940205 | -185.58% | -64.98% | 0.35x | ❌ |
