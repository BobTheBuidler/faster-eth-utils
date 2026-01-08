#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.714528041027256e-06 | 8.72168113910933e-06 | -13.06% | -11.55% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.676078253598313e-06 | 8.882140978075767e-06 | -15.71% | -13.58% | 0.86x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.750490622040916e-06 | 8.712463725119021e-06 | -12.41% | -11.04% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0011135485827166e-06 | 1.0869667218433007e-06 | -8.58% | -7.90% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2091172048649207e-06 | 1.521454893399592e-06 | -25.83% | -20.53% | 0.79x | ❌ |
| `apply_formatter_to_array[empty]` | 4.8234295737782216e-06 | 4.8893060792316886e-06 | -1.37% | -1.35% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.8916575174862696e-06 | 6.08071971108709e-06 | -3.21% | -3.11% | 0.97x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.222574770915491e-06 | 5.480405434455763e-06 | -4.94% | -4.70% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0476350421408153e-05 | 5.229880719532534e-06 | 50.08% | 100.32% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0523160180086101e-05 | 4.6881105268017145e-06 | 55.45% | 124.46% | 2.24x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.434068302205521e-06 | 5.757927283458829e-06 | 31.73% | 46.48% | 1.46x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.818258955654128e-06 | 6.134849489661439e-06 | 30.43% | 43.74% | 1.44x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.35191130934936e-06 | 6.523822748345692e-06 | 30.24% | 43.35% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.757796340370189e-06 | 7.0273393904162925e-06 | 27.98% | 38.85% | 1.39x | ✅ |
| `apply_key_map[empty]` | 1.426278860354223e-05 | 8.385833719375886e-06 | 41.20% | 70.08% | 1.70x | ✅ |
| `apply_key_map[single-key]` | 1.7590334038083333e-05 | 1.0567154131665475e-05 | 39.93% | 66.46% | 1.66x | ✅ |
| `apply_key_map[two-keys]` | 1.9967316306278604e-05 | 1.1673470137979198e-05 | 41.54% | 71.05% | 1.71x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9191086672025845e-05 | 1.1163567988056241e-05 | 41.83% | 71.91% | 1.72x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6485892931641376e-06 | 1.5501552376281047e-06 | 5.97% | 6.35% | 1.06x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.142452844199037e-06 | 1.8823958670741216e-06 | 12.14% | 13.82% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036526974459051033 | 0.001414199734512151 | -287.17% | -74.17% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005602967931512721 | 0.001612558429260217 | -187.80% | -65.25% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00045544604278967445 | 0.0016791788929157096 | -268.69% | -72.88% | 0.27x | ❌ |
