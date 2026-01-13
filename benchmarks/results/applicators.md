#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.649923554867064e-06 | 8.576220987550108e-06 | -12.11% | -10.80% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.639623234562017e-06 | 8.699644130847397e-06 | -13.88% | -12.18% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.533247513332941e-06 | 8.769496216670014e-06 | -16.41% | -14.10% | 0.86x | ❌ |
| `apply_formatter_if[condition-false]` | 9.830920643215284e-07 | 9.980829279918606e-07 | -1.52% | -1.50% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.154604744541009e-06 | 1.4140676323119705e-06 | -22.47% | -18.35% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.799319237850966e-06 | 4.8485114265359635e-06 | -1.02% | -1.01% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.928644345125461e-06 | 6.17357704646023e-06 | -4.13% | -3.97% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.161529098336467e-06 | 5.372867859709627e-06 | -4.09% | -3.93% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0666245614371805e-05 | 5.326580090377673e-06 | 50.06% | 100.25% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0790262381975084e-05 | 4.767303288518954e-06 | 55.82% | 126.34% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.514226993819075e-06 | 5.8010353543619644e-06 | 31.87% | 46.77% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.828118283500137e-06 | 6.049311244928008e-06 | 31.48% | 45.94% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.326315368791827e-06 | 6.5621507980621765e-06 | 29.64% | 42.12% | 1.42x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.820354458925608e-06 | 7.003062536964503e-06 | 28.69% | 40.23% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.4397846564931071e-05 | 8.339041721185359e-06 | 42.08% | 72.66% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.7623238283047055e-05 | 1.0624994099587115e-05 | 39.71% | 65.87% | 1.66x | ✅ |
| `apply_key_map[two-keys]` | 1.9896885215740777e-05 | 1.2199325389718528e-05 | 38.69% | 63.10% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.894712220017699e-05 | 1.1258032193554403e-05 | 40.58% | 68.30% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6529409969733926e-06 | 1.5462550927768892e-06 | 6.45% | 6.90% | 1.07x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1496052386706945e-06 | 1.9181007939804645e-06 | 10.77% | 12.07% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003721315846542171 | 0.0014268898021313205 | -283.44% | -73.92% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005606126642231991 | 0.001630930752902971 | -190.92% | -65.63% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00046207887305307123 | 0.001732844001677625 | -275.01% | -73.33% | 0.27x | ❌ |
