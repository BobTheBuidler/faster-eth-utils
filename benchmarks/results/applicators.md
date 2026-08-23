#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.319327147590342e-06 | 8.161540103655536e-06 | -11.51% | -10.32% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.332079374655992e-06 | 8.19594277399133e-06 | -11.78% | -10.54% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.320482153771985e-06 | 8.162226836549385e-06 | -11.50% | -10.31% | 0.90x | ❌ |
| `apply_formatter_if[condition-false]` | 1.0500663210136222e-06 | 1.0612540710121952e-06 | -1.07% | -1.05% | 0.99x | ❌ |
| `apply_formatter_if[condition-true]` | 1.2950464309376028e-06 | 1.5129851605795837e-06 | -16.83% | -14.40% | 0.86x | ❌ |
| `apply_formatter_to_array[empty]` | 4.546891979893147e-06 | 4.678967348764279e-06 | -2.90% | -2.82% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.821194182411345e-06 | 5.9183612761261415e-06 | -1.67% | -1.64% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.954239512538904e-06 | 5.0836529270344464e-06 | -2.61% | -2.55% | 0.97x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0135558121064722e-05 | 4.821558872743794e-06 | 52.43% | 110.21% | 2.10x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.703728872811534e-06 | 4.284442999430378e-06 | 55.85% | 126.49% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.066454201702352e-06 | 5.424410969516557e-06 | 32.75% | 48.71% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.701767546037043e-06 | 5.758051452257104e-06 | 33.83% | 51.12% | 1.51x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.260891143982784e-06 | 6.270676654027768e-06 | 32.29% | 47.69% | 1.48x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.81491352937271e-06 | 6.601513853960533e-06 | 32.74% | 48.68% | 1.49x | ✅ |
| `apply_key_map[empty]` | 1.5183681424902509e-05 | 8.263500917148366e-06 | 45.58% | 83.74% | 1.84x | ✅ |
| `apply_key_map[single-key]` | 1.7123640128283844e-05 | 1.0020353168870453e-05 | 41.48% | 70.89% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.9170647438017187e-05 | 1.1477532467465846e-05 | 40.13% | 67.03% | 1.67x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8386468753869935e-05 | 1.0816376157400705e-05 | 41.17% | 69.99% | 1.70x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.7547200435983774e-06 | 1.5432245243068996e-06 | 12.05% | 13.70% | 1.14x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.283060406855938e-06 | 1.9428529633062827e-06 | 14.90% | 17.51% | 1.18x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0002827670731204406 | 0.0009816675878281827 | -247.16% | -71.20% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00045445122695491073 | 0.001348665556187473 | -196.77% | -66.30% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00035568462222250046 | 0.001093904191406166 | -207.55% | -67.48% | 0.33x | ❌ |
