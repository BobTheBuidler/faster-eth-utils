#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.861096694911062e-06 | 8.70315318482436e-06 | -10.71% | -9.68% | 0.90x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.76133450980918e-06 | 8.81846969623799e-06 | -13.62% | -11.99% | 0.88x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.859545281539845e-06 | 8.908779450894113e-06 | -13.35% | -11.78% | 0.88x | ❌ |
| `apply_formatter_if[condition-false]` | 9.022336109671161e-07 | 9.62169110493318e-07 | -6.64% | -6.23% | 0.94x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1057727596275413e-06 | 1.387339082250611e-06 | -25.46% | -20.30% | 0.80x | ❌ |
| `apply_formatter_to_array[empty]` | 5.1993061568063205e-06 | 5.108311316516132e-06 | 1.75% | 1.78% | 1.02x | ✅ |
| `apply_formatter_to_array[multi-item]` | 6.065764459785844e-06 | 6.53491776896264e-06 | -7.73% | -7.18% | 0.93x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.3011266888536425e-06 | 5.6736288773889455e-06 | -7.03% | -6.57% | 0.93x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0593165101549242e-05 | 5.114056714135197e-06 | 51.72% | 107.14% | 2.07x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.017323504946895e-05 | 4.691583381221396e-06 | 53.88% | 116.84% | 2.17x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.584072210897682e-06 | 5.7350783621913325e-06 | 33.19% | 49.68% | 1.50x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 9.16996979248712e-06 | 6.115248758511894e-06 | 33.31% | 49.95% | 1.50x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.819815028667413e-06 | 6.492032589755109e-06 | 33.89% | 51.26% | 1.51x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 1.013606259099225e-05 | 6.814012009800855e-06 | 32.77% | 48.75% | 1.49x | ✅ |
| `apply_key_map[empty]` | 1.5343024688653433e-05 | 8.796720141369075e-06 | 42.67% | 74.42% | 1.74x | ✅ |
| `apply_key_map[single-key]` | 1.791070943442184e-05 | 1.0723250733747247e-05 | 40.13% | 67.03% | 1.67x | ✅ |
| `apply_key_map[two-keys]` | 1.983271456126465e-05 | 1.2208668161319613e-05 | 38.44% | 62.45% | 1.62x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9128929214682674e-05 | 1.146481696621508e-05 | 40.07% | 66.85% | 1.67x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.5635234339658851e-06 | 1.4926437939142681e-06 | 4.53% | 4.75% | 1.05x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.125045602918335e-06 | 1.8254744921181443e-06 | 14.10% | 16.41% | 1.16x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.0004029399197082352 | 0.0014603564060029863 | -262.43% | -72.41% | 0.28x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.0005990538330884945 | 0.0015940440000003263 | -166.09% | -62.42% | 0.38x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004927347856204263 | 0.0014711174546946709 | -198.56% | -66.51% | 0.33x | ❌ |
