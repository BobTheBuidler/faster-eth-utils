#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.537123766986696e-06 | 8.437777662774061e-06 | -11.95% | -10.67% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.58929717632445e-06 | 8.76836655709722e-06 | -15.54% | -13.45% | 0.87x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.5484408441803985e-06 | 8.833319173849288e-06 | -17.02% | -14.55% | 0.85x | ❌ |
| `apply_formatter_if[condition-false]` | 9.630812994463846e-07 | 1.0324610099839473e-06 | -7.20% | -6.72% | 0.93x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1517388805440795e-06 | 1.4936636889704278e-06 | -29.69% | -22.89% | 0.77x | ❌ |
| `apply_formatter_to_array[empty]` | 4.716869917317311e-06 | 4.947971276334089e-06 | -4.90% | -4.67% | 0.95x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.8155908997085075e-06 | 6.1849575642046625e-06 | -6.35% | -5.97% | 0.94x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.126843359245525e-06 | 5.474654972456692e-06 | -6.78% | -6.35% | 0.94x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.052389975738349e-05 | 5.2326430125990135e-06 | 50.28% | 101.12% | 2.01x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0617396677119036e-05 | 4.639728469578701e-06 | 56.30% | 128.84% | 2.29x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.239330271681279e-06 | 5.684345419224392e-06 | 31.01% | 44.95% | 1.45x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.767554893193408e-06 | 6.047557764129357e-06 | 31.02% | 44.98% | 1.45x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.170888533972004e-06 | 6.372685252866648e-06 | 30.51% | 43.91% | 1.44x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.692868424556157e-06 | 6.927380589907945e-06 | 28.53% | 39.92% | 1.40x | ✅ |
| `apply_key_map[empty]` | 1.424934409079824e-05 | 8.235270264633457e-06 | 42.21% | 73.03% | 1.73x | ✅ |
| `apply_key_map[single-key]` | 1.750032354877617e-05 | 1.0236485083596192e-05 | 41.51% | 70.96% | 1.71x | ✅ |
| `apply_key_map[two-keys]` | 1.968724222445311e-05 | 1.1783833995884543e-05 | 40.14% | 67.07% | 1.67x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8754892184071966e-05 | 1.0843278027198299e-05 | 42.18% | 72.96% | 1.73x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5735645238309237e-06 | 1.5604175497075424e-06 | 0.84% | 0.84% | 1.01x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.1612180352822242e-06 | 1.898115027409353e-06 | 12.17% | 13.86% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00037142313739999184 | 0.0014151370214724231 | -281.00% | -73.75% | 0.26x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000567197395121885 | 0.0016374398647265795 | -188.69% | -65.36% | 0.35x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004648923920459716 | 0.0017159538270549366 | -269.11% | -72.91% | 0.27x | ❌ |
