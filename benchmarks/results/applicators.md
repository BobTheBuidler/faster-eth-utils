#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.950831208947436e-06 | 8.824818235267931e-06 | -10.99% | -9.90% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.895750066263821e-06 | 8.742889705097224e-06 | -10.73% | -9.69% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.930871879407969e-06 | 8.845312920233617e-06 | -11.53% | -10.34% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 9.615806162020631e-07 | 9.952676152762496e-07 | -3.50% | -3.38% | 0.97x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2065507745083199e-06 | 1.4426933898152775e-06 | -19.57% | -16.37% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 5.096608346292044e-06 | 5.134140424849985e-06 | -0.74% | -0.73% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.22965643856187e-06 | 6.514290199134537e-06 | -4.57% | -4.37% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.45161534982401e-06 | 5.677497983376097e-06 | -4.14% | -3.98% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.068665615752647e-05 | 5.5457406202685735e-06 | 48.11% | 92.70% | 1.93x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0414106172748304e-05 | 4.87259519564827e-06 | 53.21% | 113.73% | 2.14x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.862063786480759e-06 | 5.747000728405149e-06 | 35.15% | 54.20% | 1.54x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.375422921494735e-06 | 6.090946318319398e-06 | 35.03% | 53.92% | 1.54x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.99811210771801e-06 | 6.522238432208476e-06 | 34.77% | 53.29% | 1.53x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0319382291173751e-05 | 6.811688544004649e-06 | 33.99% | 51.50% | 1.51x | ✅ |
| `apply_key_map[empty]` | 1.54689582674539e-05 | 8.946975761025685e-06 | 42.16% | 72.90% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.7960700264197666e-05 | 1.0811211682012604e-05 | 39.81% | 66.13% | 1.66x | ✅ |
| `apply_key_map[two-keys]` | 2.007613491224179e-05 | 1.247396875752669e-05 | 37.87% | 60.94% | 1.61x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9140528444058965e-05 | 1.1743870491369844e-05 | 38.64% | 62.98% | 1.63x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.561845699311812e-06 | 1.4861269334306498e-06 | 4.85% | 5.10% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.086077009561619e-06 | 1.9189428895701726e-06 | 8.01% | 8.71% | 1.09x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00039894320570014736 | 0.0014554510310552046 | -264.83% | -72.59% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00059577428718788 | 0.0015931501520267137 | -167.41% | -62.60% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004939231478693829 | 0.0014538729253030412 | -194.35% | -66.03% | 0.34x | ❌ |
