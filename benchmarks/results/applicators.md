#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.048234624945396e-06 | 8.390192660763314e-06 | -4.25% | -4.08% | 0.96x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.896488752252087e-06 | 8.67680588363609e-06 | -9.88% | -8.99% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.060590084438678e-06 | 8.382134283987415e-06 | -3.99% | -3.84% | 0.96x | ❌ |
| `apply_formatter_if[condition-false]` | 9.987803766342615e-07 | 9.493651547609726e-07 | 4.95% | 5.21% | 1.05x | ✅ |
| `apply_formatter_if[condition-true]` | 1.2272156993549415e-06 | 1.3947375808511905e-06 | -13.65% | -12.01% | 0.88x | ❌ |
| `apply_formatter_to_array[empty]` | 5.007593540210888e-06 | 4.781572075637685e-06 | 4.51% | 4.73% | 1.05x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.171969651243652e-06 | 6.17583388255645e-06 | -0.06% | -0.06% | 1.00x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.468236097803032e-06 | 5.390612158562482e-06 | 1.42% | 1.44% | 1.01x | ✅ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0249077579244994e-05 | 5.012704296126447e-06 | 51.09% | 104.46% | 2.04x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.791982393129935e-06 | 4.497080243104485e-06 | 54.07% | 117.74% | 2.18x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 9.115667838683972e-06 | 5.638717386741544e-06 | 38.14% | 61.66% | 1.62x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.34398910383304e-06 | 6.061059164275874e-06 | 35.13% | 54.16% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.81561163652936e-06 | 6.603053772475787e-06 | 32.73% | 48.65% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.972518055184965e-06 | 6.9015078515131865e-06 | 30.79% | 44.50% | 1.44x | ✅ |
| `apply_key_map[empty]` | 1.5347398433363783e-05 | 8.417471201042416e-06 | 45.15% | 82.33% | 1.82x | ✅ |
| `apply_key_map[single-key]` | 1.780168751452595e-05 | 1.0039874053951476e-05 | 43.60% | 77.31% | 1.77x | ✅ |
| `apply_key_map[two-keys]` | 1.9225798416089224e-05 | 1.1375001405738245e-05 | 40.83% | 69.02% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8219368108943165e-05 | 1.0755274399382163e-05 | 40.97% | 69.40% | 1.69x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7083095575764435e-06 | 1.440988337175566e-06 | 15.65% | 18.55% | 1.19x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2676344351535516e-06 | 1.8243420444882545e-06 | 19.55% | 24.30% | 1.24x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038734497227396525 | 0.001369487382945662 | -253.56% | -71.72% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000607944670048032 | 0.0015555607538470457 | -155.87% | -60.92% | 0.39x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0005052115745957727 | 0.0014174109239944563 | -180.56% | -64.36% | 0.36x | ❌ |
