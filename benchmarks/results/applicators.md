#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.61771523329862e-06 | 8.691696739898903e-06 | -14.10% | -12.36% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.641923391023238e-06 | 8.72650909452946e-06 | -14.19% | -12.43% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.734855547210065e-06 | 8.693555567853865e-06 | -12.39% | -11.03% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.72169604051259e-07 | 1.0593896566495065e-06 | -8.97% | -8.23% | 0.92x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1612571168580656e-06 | 1.4677966460743687e-06 | -26.40% | -20.88% | 0.79x | ❌ |
| `apply_formatter_to_array[empty]` | 4.739191398671578e-06 | 5.066606694032817e-06 | -6.91% | -6.46% | 0.94x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.855735214334244e-06 | 6.187254880188516e-06 | -5.66% | -5.36% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.120464068639861e-06 | 5.484852493437741e-06 | -7.12% | -6.64% | 0.93x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.1120652724218447e-05 | 5.3552183173847955e-06 | 51.84% | 107.66% | 2.08x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.092594784195614e-05 | 4.731118559412345e-06 | 56.70% | 130.94% | 2.31x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.324628537877646e-06 | 5.649423239151927e-06 | 32.14% | 47.35% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.831527741625039e-06 | 6.0535405087127915e-06 | 31.46% | 45.89% | 1.46x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.43373488585755e-06 | 6.484632460602327e-06 | 31.26% | 45.48% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.890540114651985e-06 | 6.9486982010185795e-06 | 29.74% | 42.34% | 1.42x | ✅ |
| `apply_key_map[empty]` | 1.4347942250348406e-05 | 8.48711275016051e-06 | 40.85% | 69.06% | 1.69x | ✅ |
| `apply_key_map[single-key]` | 1.7951169450236274e-05 | 1.038068433331257e-05 | 42.17% | 72.93% | 1.73x | ✅ |
| `apply_key_map[two-keys]` | 2.022822437195624e-05 | 1.1847368729185293e-05 | 41.43% | 70.74% | 1.71x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9527452806795637e-05 | 1.1119967168662322e-05 | 43.05% | 75.61% | 1.76x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.559336050144325e-06 | 1.5062968690186568e-06 | 3.40% | 3.52% | 1.04x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.119343753642832e-06 | 1.871346430148485e-06 | 11.70% | 13.25% | 1.13x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036631950241902163 | 0.0014176869185861451 | -287.01% | -74.16% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005512634264205504 | 0.0015815754616626825 | -186.90% | -65.14% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.000455288641420391 | 0.0016489978859394404 | -262.19% | -72.39% | 0.28x | ❌ |
