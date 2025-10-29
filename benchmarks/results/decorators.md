#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1666165703591812e-05 | 2.425101317215796e-05 | -107.87% | -51.89% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5221919138241963e-06 | 1.3820477866312828e-06 | 9.21% | 10.14% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.8243321412584e-06 | 1.4540020971697165e-05 | -64.77% | -39.31% | 0.61x | ❌ |
| `return_arg_type[float-pos0]` | 2.3835354880676615e-06 | 2.3262271578213403e-06 | 2.40% | 2.46% | 1.02x | ✅ |
| `return_arg_type[int-pos0]` | 2.3434456338654433e-06 | 2.104370237471759e-06 | 10.20% | 11.36% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.2716657093853392e-06 | 2.0410342102219817e-06 | 10.15% | 11.30% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 2.880107714382844e-06 | 2.7280939389974825e-06 | 5.28% | 5.57% | 1.06x | ✅ |
| `return_arg_type[str-pos1]` | 2.8844958835053556e-06 | 2.7323148581059994e-06 | 5.28% | 5.57% | 1.06x | ✅ |
