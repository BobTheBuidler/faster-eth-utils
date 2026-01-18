#### [faster_eth_utils.applicators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/applicators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_applicators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `apply_formatter_at_index[at-index-0]` | 7.640324978522343e-06 | 8.552562512676327e-06 | -11.94% | -10.67% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-1]` | 7.786828054853601e-06 | 8.758321925661045e-06 | -12.48% | -11.09% | 0.89x | ❌ |
| `apply_formatter_at_index[at-index-2]` | 7.734125964051395e-06 | 8.71101800803141e-06 | -12.63% | -11.21% | 0.89x | ❌ |
| `apply_formatter_if[condition-false]` | 9.522212160397148e-07 | 9.6752461785603e-07 | -1.61% | -1.58% | 0.98x | ❌ |
| `apply_formatter_if[condition-true]` | 1.1908505392099614e-06 | 1.3823966698532537e-06 | -16.08% | -13.86% | 0.86x | ❌ |
| `apply_formatter_to_array[empty]` | 4.792226690739436e-06 | 4.808723000419349e-06 | -0.34% | -0.34% | 1.00x | ❌ |
| `apply_formatter_to_array[multi-item]` | 5.898368582614988e-06 | 6.1873854761871685e-06 | -4.90% | -4.67% | 0.95x | ❌ |
| `apply_formatter_to_array[single-item]` | 5.201702269677424e-06 | 5.415722797066567e-06 | -4.11% | -3.95% | 0.96x | ❌ |
| `apply_formatters_to_dict[all-keys-present]` | 1.0493064627732088e-05 | 5.2462801883877494e-06 | 50.00% | 100.01% | 2.00x | ✅ |
| `apply_formatters_to_dict[key-not-present]` | 1.0548197106994041e-05 | 4.720591612714523e-06 | 55.25% | 123.45% | 2.23x | ✅ |
| `apply_formatters_to_sequence[1-item]` | 8.356187563305817e-06 | 5.6409499933645274e-06 | 32.49% | 48.13% | 1.48x | ✅ |
| `apply_formatters_to_sequence[2-items]` | 8.853234598157357e-06 | 6.032124529705971e-06 | 31.87% | 46.77% | 1.47x | ✅ |
| `apply_formatters_to_sequence[3-items]` | 9.338704312307677e-06 | 6.510010830788532e-06 | 30.29% | 43.45% | 1.43x | ✅ |
| `apply_formatters_to_sequence[4-items]` | 9.838321828817657e-06 | 6.994640797698532e-06 | 28.90% | 40.66% | 1.41x | ✅ |
| `apply_key_map[empty]` | 1.470269404625356e-05 | 8.353430273216514e-06 | 43.18% | 76.01% | 1.76x | ✅ |
| `apply_key_map[single-key]` | 1.768018053253738e-05 | 1.0701787299471896e-05 | 39.47% | 65.21% | 1.65x | ✅ |
| `apply_key_map[two-keys]` | 2.0008769832438328e-05 | 1.2199776814499549e-05 | 39.03% | 64.01% | 1.64x | ✅ |
| `apply_key_map[unrelated-key]` | 1.9153595681825322e-05 | 1.1392491309705575e-05 | 40.52% | 68.12% | 1.68x | ✅ |
| `apply_one_of_formatters[first-matches]` | 1.6069181935231634e-06 | 1.5596132974603066e-06 | 2.94% | 3.03% | 1.03x | ✅ |
| `apply_one_of_formatters[second-matches]` | 2.159883669531222e-06 | 1.9016327386593439e-06 | 11.96% | 13.58% | 1.14x | ✅ |
| `combine_argument_formatters[one-formatter]` | 0.00036107481644034693 | 0.0013414008089375749 | -271.50% | -73.08% | 0.27x | ❌ |
| `combine_argument_formatters[three-formatters]` | 0.000551062272142924 | 0.0016010812575515685 | -190.54% | -65.58% | 0.34x | ❌ |
| `combine_argument_formatters[two-formatters]` | 0.0004540196155207169 | 0.001670104186334578 | -267.85% | -72.81% | 0.27x | ❌ |
