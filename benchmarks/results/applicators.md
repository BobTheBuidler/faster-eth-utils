#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.126766557715267e-06 | 7.619657622576814e-06 | -6.92% | -6.47% | 0.94x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.121976451904872e-06 | 7.713526450659447e-06 | -8.31% | -7.67% | 0.92x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.144514347224164e-06 | 7.604479402887735e-06 | -6.44% | -6.05% | 0.94x | ❌ |
| `apply_formatter_if[condition-false]` | 8.716346013657614e-07 | 9.485028010817926e-07 | -8.82% | -8.10% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.0537193025512284e-06 | 1.402913059567838e-06 | -33.14% | -24.89% | 0.75x | ❌ |
| `apply_formatter_to_array[empty]` | 4.490859039825753e-06 | 4.448615710045808e-06 | 0.94% | 0.95% | 1.01x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.474226388212949e-06 | 5.871907592760655e-06 | -7.26% | -6.77% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.82282783618677e-06 | 4.90654477821386e-06 | -1.74% | -1.71% | 0.98x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 9.082444928747254e-06 | 4.84633691231471e-06 | 46.64% | 87.41% | 1.87x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.707794692107162e-06 | 4.356809080339149e-06 | 49.97% | 99.87% | 2.00x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 7.6124647502294254e-06 | 5.019445706129999e-06 | 34.06% | 51.66% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.116924783459681e-06 | 5.5096918789396555e-06 | 32.12% | 47.32% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.268361423626402e-06 | 6.060027806543153e-06 | 34.62% | 52.94% | 1.53x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.205139015257414e-06 | 6.432297234117645e-06 | 30.12% | 43.11% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.2943388234069441e-05 | 7.771947319009726e-06 | 39.95% | 66.54% | 1.67x | ✅ |
| `apply_key_map[single-key]` | 1.5267968682268284e-05 | 9.218294103012532e-06 | 39.62% | 65.63% | 1.66x | ✅ |
| `apply_key_map[two-keys]` | 1.73649875586626e-05 | 1.0629268120138973e-05 | 38.79% | 63.37% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.6451396251492067e-05 | 1.019734605580948e-05 | 38.02% | 61.33% | 1.61x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.4340826826713465e-06 | 1.476214693818486e-06 | -2.94% | -2.85% | 0.97x | ❌ |
| `apply_one_of_formatters[second-matches]` | 2.0225475329092803e-06 | 1.849030789335024e-06 | 8.58% | 9.38% | 1.09x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003412079278693993 | 0.0010437595885413782 | -205.90% | -67.31% | 0.33x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0004886685732116511 | 0.0011513133027787287 | -135.60% | -57.56% | 0.42x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00039824760942221225 | 0.0013499953479448816 | -238.98% | -70.50% | 0.29x | ❌ |
