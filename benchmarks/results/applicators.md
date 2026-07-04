#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.953466716575138e-06 | 8.550163683639828e-06 | -7.50% | -6.98% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.77708648087941e-06 | 8.560552859829212e-06 | -10.07% | -9.15% | 0.91x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.860485253768114e-06 | 8.606752514425592e-06 | -9.49% | -8.67% | 0.91x | ❌ |
| `apply_formatter_if[condition-false]` | 9.71285653141359e-07 | 1.0411329425505641e-06 | -7.19% | -6.71% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.176283251106464e-06 | 1.4262370027056299e-06 | -21.25% | -17.53% | 0.82x | ❌ |
| `apply_formatter_to_array[empty]` | 4.931813531942208e-06 | 4.921737486978416e-06 | 0.20% | 0.20% | 1.00x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.029572681255876e-06 | 6.2472732103782065e-06 | -3.61% | -3.48% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.264665886938825e-06 | 5.3909311494810585e-06 | -2.40% | -2.34% | 0.98x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0495937631682488e-05 | 5.082934745070462e-06 | 51.57% | 106.49% | 2.06x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0148563255872865e-05 | 4.545893933113497e-06 | 55.21% | 123.25% | 2.23x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.482663331461504e-06 | 5.655053819771796e-06 | 33.33% | 50.00% | 1.50x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.993171146537607e-06 | 6.140881540544973e-06 | 31.72% | 46.45% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.53965106752984e-06 | 6.593346795388442e-06 | 30.88% | 44.69% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.907478874591145e-06 | 7.010939958811583e-06 | 29.24% | 41.31% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.5064553936691162e-05 | 8.826313298809128e-06 | 41.41% | 70.68% | 1.71x | ✅ |
| `apply_key_map[single-key]` | 1.7678172273088338e-05 | 1.0553784019762834e-05 | 40.30% | 67.51% | 1.68x | ✅ |
| `apply_key_map[two-keys]` | 1.9822979087104832e-05 | 1.1944936326842753e-05 | 39.74% | 65.95% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.884400418394047e-05 | 1.1240953498094063e-05 | 40.35% | 67.64% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.600087810711054e-06 | 1.5172004085741486e-06 | 5.18% | 5.46% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.132104436406648e-06 | 1.908626577118516e-06 | 10.48% | 11.71% | 1.12x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00039832701460301316 | 0.001478193920338931 | -271.10% | -73.05% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005735317875977923 | 0.0015650083289469624 | -172.87% | -63.35% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004693175654732361 | 0.0014402457540716935 | -206.88% | -67.41% | 0.33x | ❌ |
