#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.842692422781161e-06 | 8.871507922532894e-06 | -13.12% | -11.60% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.787292483432395e-06 | 8.928907726302725e-06 | -14.66% | -12.79% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.85576834347277e-06 | 8.849947667393778e-06 | -12.66% | -11.23% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.556931783045135e-07 | 9.866159868995094e-07 | -3.24% | -3.13% | 0.97x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1887697635372042e-06 | 1.415900350373073e-06 | -19.11% | -16.04% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.921728591806965e-06 | 5.32951442058304e-06 | -8.29% | -7.65% | 0.92x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.98542589645641e-06 | 6.734732181261982e-06 | -12.52% | -11.13% | 0.89x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.2526689599824425e-06 | 5.864158192871702e-06 | -11.64% | -10.43% | 0.90x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0383672606385285e-05 | 5.1843601359353274e-06 | 50.07% | 100.29% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.946110482399963e-06 | 4.718755405000663e-06 | 52.56% | 110.78% | 2.11x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.315748709560154e-06 | 6.075584542028744e-06 | 26.94% | 36.87% | 1.37x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.806885860754565e-06 | 6.489991395110326e-06 | 26.31% | 35.70% | 1.36x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.364345554861254e-06 | 6.865130365317096e-06 | 26.69% | 36.40% | 1.36x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.738066477032787e-06 | 7.380783967724112e-06 | 24.21% | 31.94% | 1.32x | ✅ |
| `apply_key_map[empty]` | 1.4186188590054349e-05 | 8.21917449751118e-06 | 42.06% | 72.60% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.6716951968991084e-05 | 1.0096167221274191e-05 | 39.61% | 65.58% | 1.66x | ✅ |
| `apply_key_map[two-keys]` | 1.8739529664345323e-05 | 1.1455789061720177e-05 | 38.87% | 63.58% | 1.64x | ✅ |
| `apply_key_map[unrelated-key]` | 1.7748648941869093e-05 | 1.0565247329468117e-05 | 40.47% | 67.99% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6192706598114674e-06 | 1.5126288211320173e-06 | 6.59% | 7.05% | 1.07x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2357347177921284e-06 | 1.8555617642675202e-06 | 17.00% | 20.49% | 1.20x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003607261344536401 | 0.001439088469840811 | -298.94% | -74.93% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005712798170644238 | 0.0016352054512827523 | -186.24% | -65.06% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045972631933337315 | 0.0018004500084313178 | -291.64% | -74.47% | 0.26x | ❌ |
