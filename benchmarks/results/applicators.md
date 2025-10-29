#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 8.0076530204054e-06 | 8.623238100946047e-06 | -7.69% | -7.14% | 0.93x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 8.050268875842526e-06 | 8.554360080987196e-06 | -6.26% | -5.89% | 0.94x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 8.532803739330935e-06 | 8.490069640609927e-06 | 0.50% | 0.50% | 1.01x | ✅ |
| `apply_formatter_if[condition-false]` | 9.754367155369377e-07 | 9.259749583031406e-07 | 5.07% | 5.34% | 1.05x | ✅ |
| `apply_formatter_if[condition-true]` | 1.184905221272262e-06 | 1.4135065429991077e-06 | -19.29% | -16.17% | 0.84x | ❌ |
| `apply_formatter_to_array[empty]` | 4.948088734555848e-06 | 4.782289421887672e-06 | 3.35% | 3.47% | 1.03x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.107885144101008e-06 | 6.236595422635211e-06 | -2.11% | -2.06% | 0.98x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.347659007368822e-06 | 5.419214892108624e-06 | -1.34% | -1.32% | 0.99x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0167880279103216e-05 | 5.028162916032114e-06 | 50.55% | 102.22% | 2.02x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 9.732563558800325e-06 | 4.48955641058227e-06 | 53.87% | 116.78% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.76019975838968e-06 | 5.541722140253568e-06 | 36.74% | 58.08% | 1.58x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.230048117556536e-06 | 5.92914640291752e-06 | 35.76% | 55.67% | 1.56x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.669381170972247e-06 | 6.3583149240337976e-06 | 34.24% | 52.07% | 1.52x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.0002577403359829e-05 | 6.732843237837477e-06 | 32.69% | 48.56% | 1.49x | ✅ |
| `apply_key_map[empty]` | 1.4460446601910637e-05 | 8.265505972139864e-06 | 42.84% | 74.95% | 1.75x | ✅ |
| `apply_key_map[single-key]` | 1.6924492837882378e-05 | 9.753816311859357e-06 | 42.37% | 73.52% | 1.74x | ✅ |
| `apply_key_map[two-keys]` | 1.922617170300632e-05 | 1.1548276582290635e-05 | 39.93% | 66.49% | 1.66x | ✅ |
| `apply_key_map[unrelated-key]` | 1.8357387193828324e-05 | 1.0545961864504029e-05 | 42.55% | 74.07% | 1.74x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6276647806609752e-06 | 1.4846302141952712e-06 | 8.79% | 9.63% | 1.10x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.2411893803118994e-06 | 1.821207711848144e-06 | 18.74% | 23.06% | 1.23x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0003709502746425878 | 0.0012984199389427468 | -250.03% | -71.43% | 0.29x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005755167092572429 | 0.001551069219709404 | -169.51% | -62.90% | 0.37x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.00048178896726604984 | 0.0015378227587936621 | -219.19% | -68.67% | 0.31x | ❌ |
