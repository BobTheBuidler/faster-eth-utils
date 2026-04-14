#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.029223016635528e-06 | 8.741774815496353e-06 | -8.87% | -8.15% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.89546823993396e-06 | 8.84369084828034e-06 | -12.01% | -10.72% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.871475811756853e-06 | 8.669278578094056e-06 | -10.14% | -9.20% | 0.91x | ❌ |
| `apply_formatter_if[condition-false]` | 9.281664726369335e-07 | 9.486826680671015e-07 | -2.21% | -2.16% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1306557372050608e-06 | 1.3829230013246207e-06 | -22.31% | -18.24% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.952071498497628e-06 | 5.0196372281092005e-06 | -1.36% | -1.35% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.910126366674784e-06 | 6.264959322807413e-06 | -6.00% | -5.66% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.270958697992834e-06 | 5.503583255275745e-06 | -4.41% | -4.23% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.030444337061377e-05 | 5.339945692480327e-06 | 48.18% | 92.97% | 1.93x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.971790784655838e-06 | 4.75759871455154e-06 | 52.29% | 109.60% | 2.10x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.45104643698248e-06 | 5.8986779561308e-06 | 30.20% | 43.27% | 1.43x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.868314627857468e-06 | 6.219811436781499e-06 | 29.86% | 42.58% | 1.43x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.476380986344895e-06 | 6.6239327038400025e-06 | 30.10% | 43.06% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0020287353144491e-05 | 7.071682938184683e-06 | 29.43% | 41.70% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4466785395906272e-05 | 8.29117591016349e-06 | 42.69% | 74.48% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.694560937893575e-05 | 9.86493532731275e-06 | 41.78% | 71.78% | 1.72x | ✅ |
| `apply_key_map[two-keys]` | 1.9277272926759215e-05 | 1.1295577875036539e-05 | 41.40% | 70.66% | 1.71x | ✅ |
| `apply_key_map[unrelated-key]` | 1.7988735144570972e-05 | 1.043289115518139e-05 | 42.00% | 72.42% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6013477806496208e-06 | 1.4655164458578115e-06 | 8.48% | 9.27% | 1.09x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.113207503521967e-06 | 1.797008257296437e-06 | 14.96% | 17.60% | 1.18x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003809561894271209 | 0.0014297061315374237 | -275.29% | -73.35% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005733315430027195 | 0.0016525739256765559 | -188.24% | -65.31% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004636642210079694 | 0.0017775103802816202 | -283.36% | -73.91% | 0.26x | ❌ |
