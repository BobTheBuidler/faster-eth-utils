#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.845332433370193e-06 | 8.95724627103344e-06 | -14.17% | -12.41% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.840898316662828e-06 | 8.940555906279093e-06 | -14.02% | -12.30% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.749421641297958e-06 | 8.828620123285939e-06 | -13.93% | -12.22% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.496180602684088e-07 | 9.864412993233061e-07 | -3.88% | -3.73% | 0.96x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1821065352567717e-06 | 1.4092858680570538e-06 | -19.22% | -16.12% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.861682971397901e-06 | 5.0506282687868504e-06 | -3.89% | -3.74% | 0.96x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.927221062351772e-06 | 6.230139127295389e-06 | -5.11% | -4.86% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.159448664942506e-06 | 5.462533431131611e-06 | -5.87% | -5.55% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.169908855962821e-05 | 5.134802239697885e-06 | 56.11% | 127.84% | 2.28x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.720118807943876e-06 | 4.69136354121469e-06 | 51.74% | 107.19% | 2.07x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.378037433856957e-06 | 5.830619915506939e-06 | 30.41% | 43.69% | 1.44x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.941834699529445e-06 | 6.20980931789519e-06 | 30.55% | 44.00% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.430694913429532e-06 | 6.6342653587619875e-06 | 29.65% | 42.15% | 1.42x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.819397572673524e-06 | 7.0533512384687654e-06 | 28.17% | 39.22% | 1.39x | ✅ |
| `apply_key_map[empty]` | 1.4152016338562035e-05 | 8.458910355549554e-06 | 40.23% | 67.30% | 1.67x | ✅ |
| `apply_key_map[single-key]` | 1.7046962205907794e-05 | 1.056911736066595e-05 | 38.00% | 61.29% | 1.61x | ✅ |
| `apply_key_map[two-keys]` | 1.9217354937805637e-05 | 1.160196941355224e-05 | 39.63% | 65.64% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8663200020187903e-05 | 1.0792218272340961e-05 | 42.17% | 72.93% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6704361002208524e-06 | 1.4682027257336028e-06 | 12.11% | 13.77% | 1.14x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.076490029196025e-06 | 1.8092497851009797e-06 | 12.87% | 14.77% | 1.15x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003724251480756427 | 0.001465151968895963 | -293.41% | -74.58% | 0.25x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005662204168997708 | 0.001694955292599246 | -199.35% | -66.59% | 0.33x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004566672202800218 | 0.0018586669650345728 | -307.01% | -75.43% | 0.25x | ❌ |
