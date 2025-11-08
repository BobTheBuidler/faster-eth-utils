#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.035420058129297e-06 | 8.457377016523045e-06 | -5.25% | -4.99% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.001184638868372e-06 | 8.468161013890073e-06 | -5.84% | -5.51% | 0.94x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.924146174835288e-06 | 8.36961076849403e-06 | -5.62% | -5.32% | 0.95x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0076125271225205e-06 | 9.559375813477084e-07 | 5.13% | 5.41% | 1.05x | ✅ |
| `apply_formatter_if[condition-true]` | 1.252890125633184e-06 | 1.404598838387069e-06 | -12.11% | -10.80% | 0.89x | ❌ |
| `apply_formatter_to_array[empty]` | 4.955303312838578e-06 | 4.7497152890553285e-06 | 4.15% | 4.33% | 1.04x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.131896220820055e-06 | 6.999170382819494e-06 | -14.14% | -12.39% | 0.88x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.388145362764586e-06 | 5.5320063088730014e-06 | -2.67% | -2.60% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.027259034765913e-05 | 4.9621983506413884e-06 | 51.69% | 107.02% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.812264011765094e-06 | 4.481909755416604e-06 | 54.32% | 118.93% | 2.19x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.46986815860171e-06 | 5.558570746040613e-06 | 34.37% | 52.37% | 1.52x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.07949089149635e-06 | 5.939971536218372e-06 | 34.58% | 52.85% | 1.53x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.546464723081963e-06 | 6.407039193021757e-06 | 32.89% | 49.00% | 1.49x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.824417119951178e-06 | 6.72271995035839e-06 | 31.57% | 46.14% | 1.46x | ✅ |
| `apply_key_map[empty]` | 1.4594995879282913e-05 | 8.450010851035547e-06 | 42.10% | 72.72% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.7043001921259002e-05 | 1.0007041819392773e-05 | 41.28% | 70.31% | 1.70x | ✅ |
| `apply_key_map[two-keys]` | 1.9125545461707815e-05 | 1.1757489347844982e-05 | 38.52% | 62.67% | 1.63x | ✅ |
| `apply_key_map[unrelated-key]` | 1.807705304064031e-05 | 1.064966002208018e-05 | 41.09% | 69.74% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.8188389492379532e-06 | 1.4624216676247028e-06 | 19.60% | 24.37% | 1.24x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.269863129195398e-06 | 1.8328245131519642e-06 | 19.25% | 23.85% | 1.24x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003609725629439246 | 0.0013926733098148718 | -285.81% | -74.08% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0006056119293762683 | 0.0016713482679848526 | -175.98% | -63.77% | 0.36x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004939168292244862 | 0.0014630270441432826 | -196.21% | -66.24% | 0.34x | ❌ |
