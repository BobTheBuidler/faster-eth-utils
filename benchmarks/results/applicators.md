#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.021682279869161e-06 | 9.16285916781202e-06 | -14.23% | -12.45% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.049671644952276e-06 | 9.251594936935364e-06 | -14.93% | -12.99% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.01518267184845e-06 | 9.177779961597157e-06 | -14.50% | -12.67% | 0.87x | ❌ |
| `apply_formatter_if[condition-false]` | 9.615784785208227e-07 | 1.000835959864353e-06 | -4.08% | -3.92% | 0.96x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1776335440419653e-06 | 1.4132942040852325e-06 | -20.01% | -16.67% | 0.83x | ❌ |
| `apply_formatter_to_array[empty]` | 5.038308232652549e-06 | 5.096202265621854e-06 | -1.15% | -1.14% | 0.99x | ❌ |
| `apply_formatter_to_array[multi-item]` | 6.354403914888562e-06 | 6.612590399162024e-06 | -4.06% | -3.90% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.490525676305338e-06 | 5.716016633097458e-06 | -4.11% | -3.94% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0824179790108642e-05 | 5.041093219749214e-06 | 53.43% | 114.72% | 2.15x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0381288408121457e-05 | 4.599574805650302e-06 | 55.69% | 125.70% | 2.26x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.78306266531528e-06 | 5.911181309720853e-06 | 32.70% | 48.58% | 1.49x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.207853906354055e-06 | 6.237463712087474e-06 | 32.26% | 47.62% | 1.48x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.85694532349381e-06 | 6.798430141494842e-06 | 31.03% | 44.99% | 1.45x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0195976974664744e-05 | 6.888490711921327e-06 | 32.44% | 48.01% | 1.48x | ✅ |
| `apply_key_map[empty]` | 1.5004354580388414e-05 | 9.234369062010077e-06 | 38.46% | 62.48% | 1.62x | ✅ |
| `apply_key_map[single-key]` | 1.7826432227791852e-05 | 1.0917345163399235e-05 | 38.76% | 63.29% | 1.63x | ✅ |
| `apply_key_map[two-keys]` | 1.984082004978006e-05 | 1.2741123378148198e-05 | 35.78% | 55.72% | 1.56x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8798262811003593e-05 | 1.1905445941128478e-05 | 36.67% | 57.90% | 1.58x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6903692097929357e-06 | 1.4933081803530262e-06 | 11.66% | 13.20% | 1.13x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.147249384310831e-06 | 1.8939539112688934e-06 | 11.80% | 13.37% | 1.13x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.000406905585119997 | 0.0014684595489893263 | -260.88% | -72.29% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000597658192634367 | 0.0015729969269169008 | -163.19% | -62.01% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004937618806881833 | 0.0014655279696047538 | -196.81% | -66.31% | 0.34x | ❌ |
