#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1720101686439181e-05 | 2.441462745001786e-05 | -108.31% | -52.00% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5666174622785116e-06 | 1.4540545678921104e-06 | 7.19% | 7.74% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.561250494094612e-06 | 1.4678065441404634e-05 | -71.45% | -41.67% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.5250539313985862e-06 | 2.1881629506654284e-06 | 13.34% | 15.40% | 1.15x | ✅ |
| `return_arg_type[int-pos0]` | 2.4576154022174958e-06 | 2.113153338286873e-06 | 14.02% | 16.30% | 1.16x | ✅ |
| `return_arg_type[int-pos1]` | 2.4139958664506356e-06 | 2.1298793654422598e-06 | 11.77% | 13.34% | 1.13x | ✅ |
| `return_arg_type[str-pos0]` | 3.218035789156162e-06 | 2.789813548061671e-06 | 13.31% | 15.35% | 1.15x | ✅ |
| `return_arg_type[str-pos1]` | 3.1863226819215116e-06 | 2.7559801435288328e-06 | 13.51% | 15.61% | 1.16x | ✅ |
