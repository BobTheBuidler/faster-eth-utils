#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.990521884630844e-06 | 8.565051764496498e-06 | -7.19% | -6.71% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.965573443421506e-06 | 8.574642898927521e-06 | -7.65% | -7.10% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.05939870265954e-06 | 8.58365138566052e-06 | -6.50% | -6.11% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 9.346325304019697e-07 | 9.624501679713529e-07 | -2.98% | -2.89% | 0.97x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1424601284574188e-06 | 1.3971665976540475e-06 | -22.29% | -18.23% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.48841504113238e-06 | 4.593755996540475e-06 | -2.35% | -2.29% | 0.98x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.525006958558995e-06 | 5.985159849728256e-06 | -8.33% | -7.69% | 0.92x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.87651719143469e-06 | 5.16896083641255e-06 | -6.00% | -5.66% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.026914853314029e-05 | 4.930657838329681e-06 | 51.99% | 108.27% | 2.08x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0032683675459788e-05 | 4.427724873009881e-06 | 55.87% | 126.59% | 2.27x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.157619110945266e-06 | 5.2926926147779556e-06 | 35.12% | 54.13% | 1.54x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.590610046778417e-06 | 5.6855028219792006e-06 | 33.82% | 51.10% | 1.51x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.168827600401612e-06 | 6.160451348262735e-06 | 32.81% | 48.83% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.683596539972337e-06 | 6.4654979134667614e-06 | 33.23% | 49.77% | 1.50x | ✅ |
| `apply_key_map[empty]` | 1.4787725406310565e-05 | 8.304784483560003e-06 | 43.84% | 78.06% | 1.78x | ✅ |
| `apply_key_map[single-key]` | 1.7052882692194127e-05 | 9.979551102098773e-06 | 41.48% | 70.88% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9280013909660694e-05 | 1.137590964449098e-05 | 41.00% | 69.48% | 1.69x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8243460571255957e-05 | 1.0775673625699222e-05 | 40.93% | 69.30% | 1.69x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.611921035728781e-06 | 1.4806450141701322e-06 | 8.14% | 8.87% | 1.09x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.079524249676129e-06 | 1.9585829313593467e-06 | 5.82% | 6.17% | 1.06x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0002938183588519033 | 0.0010133621805569328 | -244.89% | -71.01% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00044911312738440755 | 0.0014114416301376088 | -214.27% | -68.18% | 0.32x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000358005299790942 | 0.0011147964714087557 | -211.39% | -67.89% | 0.32x | ❌ |
