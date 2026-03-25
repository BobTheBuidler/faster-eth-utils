#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.838840375392852e-06 | 8.905629064932938e-06 | -13.61% | -11.98% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.893366513833498e-06 | 9.033396597659485e-06 | -14.44% | -12.62% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.784126763290476e-06 | 8.768102218154427e-06 | -12.64% | -11.22% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.350524389290644e-07 | 1.0007200853806178e-06 | -7.02% | -6.56% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1581516429845774e-06 | 1.4262257905145619e-06 | -23.15% | -18.80% | 0.81x | ❌ |
| `apply_formatter_to_array[empty]` | 4.895500049709468e-06 | 5.020132097373811e-06 | -2.55% | -2.48% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.097970973785825e-06 | 6.323360742947497e-06 | -3.70% | -3.56% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.281358737001764e-06 | 5.5352046814071775e-06 | -4.81% | -4.59% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0362719717506827e-05 | 5.215081230898319e-06 | 49.67% | 98.71% | 1.99x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.916971538669418e-06 | 4.821106652682984e-06 | 51.39% | 105.70% | 2.06x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.129188441213457e-06 | 5.6824131181389985e-06 | 30.10% | 43.06% | 1.43x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.749035459663528e-06 | 6.064192343780247e-06 | 30.69% | 44.27% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 8.980188397754034e-06 | 6.35003841467051e-06 | 29.29% | 41.42% | 1.41x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.749419569195787e-06 | 6.825015703802268e-06 | 30.00% | 42.85% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.4334185371413678e-05 | 8.217836783617122e-06 | 42.67% | 74.43% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.6772354286025093e-05 | 9.902637000629215e-06 | 40.96% | 69.37% | 1.69x | ✅ |
| `apply_key_map[two-keys]` | 1.8794119586080676e-05 | 1.1367316397705393e-05 | 39.52% | 65.33% | 1.65x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8255395111272632e-05 | 1.0636147128247436e-05 | 41.74% | 71.64% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6947268766006295e-06 | 1.49597328256641e-06 | 11.73% | 13.29% | 1.13x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.176015647362866e-06 | 1.9003531057803336e-06 | 12.67% | 14.51% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003784720212431987 | 0.0013668478113762167 | -261.15% | -72.31% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000556509869594743 | 0.001584181382776677 | -184.66% | -64.87% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004628514281369168 | 0.0016701360214167278 | -260.84% | -72.29% | 0.28x | ❌ |
