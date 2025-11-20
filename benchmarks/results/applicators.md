#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.183277626974739e-06 | 7.441578906197357e-06 | -3.60% | -3.47% | 0.97x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.18117076408362e-06 | 7.529366700359893e-06 | -4.85% | -4.62% | 0.95x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.1408903604648494e-06 | 7.418926679828975e-06 | -3.89% | -3.75% | 0.96x | ❌ |
| `apply_formatter_if[condition-false]` | 8.508641942532359e-07 | 9.031665946311878e-07 | -6.15% | -5.79% | 0.94x | ❌ |
| `apply_formatter_if[condition-true]` | 1.0414417138196864e-06 | 1.4071710593669946e-06 | -35.12% | -25.99% | 0.74x | ❌ |
| `apply_formatter_to_array[empty]` | 4.4735315322323505e-06 | 4.38284418174562e-06 | 2.03% | 2.07% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 5.591171482441947e-06 | 5.8561101469328635e-06 | -4.74% | -4.52% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 4.829779195528139e-06 | 4.87900343386935e-06 | -1.02% | -1.01% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 9.178124833155183e-06 | 4.6607020747743954e-06 | 49.22% | 96.93% | 1.97x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 8.767633100159006e-06 | 4.1449402154485385e-06 | 52.72% | 111.53% | 2.12x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 7.60747798773881e-06 | 4.931734931330306e-06 | 35.17% | 54.26% | 1.54x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.165073956316696e-06 | 5.441453741690252e-06 | 33.36% | 50.05% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.004938133486097e-06 | 5.986192115008194e-06 | 33.52% | 50.43% | 1.50x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.20251712404591e-06 | 6.419402985584271e-06 | 30.24% | 43.35% | 1.43x | ✅ |
| `apply_key_map[empty]` | 1.3989481889125337e-05 | 8.004230691348435e-06 | 42.78% | 74.78% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.6122181753730023e-05 | 9.343799661111435e-06 | 42.04% | 72.54% | 1.73x | ✅ |
| `apply_key_map[two-keys]` | 1.8126459930948618e-05 | 1.0773391515325156e-05 | 40.57% | 68.25% | 1.68x | ✅ |
| `apply_key_map[unrelated-key]` | 1.769137780122665e-05 | 9.984565206571002e-06 | 43.56% | 77.19% | 1.77x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.4177413579661313e-06 | 1.4871882700631179e-06 | -4.90% | -4.67% | 0.95x | ❌ |
| `apply_one_of_formatters[second-matches]` | 1.9159763318672484e-06 | 1.8030746963729694e-06 | 5.89% | 6.26% | 1.06x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003271374289392377 | 0.000983629101152404 | -200.68% | -66.74% | 0.33x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000491303451004083 | 0.0012582976632267027 | -156.11% | -60.95% | 0.39x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004270775544793764 | 0.0011649230267642536 | -172.77% | -63.34% | 0.37x | ❌ |
