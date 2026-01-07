#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2198290813940463e-05 | 2.5341010041220883e-05 | -107.74% | -51.86% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6366416780816007e-06 | 1.4639144229686727e-06 | 10.55% | 11.80% | 1.12x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.509160827063372e-06 | 1.4682364934224012e-05 | -72.55% | -42.05% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4478511684592174e-06 | 2.2859947731651682e-06 | 6.61% | 7.08% | 1.07x | ✅ |
| `return_arg_type[int-pos0]` | 2.3825237070061327e-06 | 2.2441102791584997e-06 | 5.81% | 6.17% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.2977809804495474e-06 | 2.1631901020580923e-06 | 5.86% | 6.22% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 3.102247909872643e-06 | 2.8454340688420996e-06 | 8.28% | 9.03% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.1880246810096044e-06 | 2.837210039098506e-06 | 11.00% | 12.36% | 1.12x | ✅ |
