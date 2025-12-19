#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.566474441979724e-06 | 8.607050840127756e-06 | -13.75% | -12.09% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.590378828775089e-06 | 8.541345729145115e-06 | -12.53% | -11.13% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.552270730368099e-06 | 8.611445244738324e-06 | -14.02% | -12.30% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.382332775747478e-07 | 1.0340673136443999e-06 | -10.21% | -9.27% | 0.91x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1321266273143306e-06 | 1.478837309360206e-06 | -30.62% | -23.44% | 0.77x | ❌ |
| `apply_formatter_to_array[empty]` | 4.765788020251409e-06 | 4.910169068679804e-06 | -3.03% | -2.94% | 0.97x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.8262295584973516e-06 | 6.07770339852143e-06 | -4.32% | -4.14% | 0.96x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.16746865484039e-06 | 5.463909365618334e-06 | -5.74% | -5.43% | 0.95x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0373934363181433e-05 | 5.3869445521743e-06 | 48.07% | 92.58% | 1.93x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0503117644374496e-05 | 4.8068747864816105e-06 | 54.23% | 118.50% | 2.19x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.298737300120096e-06 | 5.629893952417597e-06 | 32.16% | 47.40% | 1.47x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.806290209244572e-06 | 5.992751453220114e-06 | 31.95% | 46.95% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.359346885545251e-06 | 6.358342578915145e-06 | 32.06% | 47.20% | 1.47x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.6161073367455e-06 | 6.877589893829174e-06 | 28.48% | 39.82% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.426811099537599e-05 | 8.123891127458086e-06 | 43.06% | 75.63% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.7340230135124485e-05 | 1.0529228546297768e-05 | 39.28% | 64.69% | 1.65x | ✅ |
| `apply_key_map[two-keys]` | 1.982800184657766e-05 | 1.1648098053861379e-05 | 41.25% | 70.23% | 1.70x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9067288863452515e-05 | 1.1040190518370048e-05 | 42.10% | 72.71% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5681212631695953e-06 | 1.4758035505040728e-06 | 5.89% | 6.26% | 1.06x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.115619930159759e-06 | 1.7932347193721976e-06 | 15.24% | 17.98% | 1.18x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00038831419812993017 | 0.0014299235597576355 | -268.24% | -72.84% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.00056258019418781 | 0.0016600344112476595 | -195.08% | -66.11% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004666156697353697 | 0.0017052460514948293 | -265.45% | -72.64% | 0.27x | ❌ |
