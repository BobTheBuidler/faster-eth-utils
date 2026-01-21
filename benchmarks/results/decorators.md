#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1810435307580677e-05 | 2.480158375653299e-05 | -110.00% | -52.38% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6207072940554527e-06 | 1.4755472767429145e-06 | 8.96% | 9.84% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.380487945165382e-06 | 1.481373939608397e-05 | -76.76% | -43.43% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4492653208805623e-06 | 2.24573842747775e-06 | 8.31% | 9.06% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.3876772791481248e-06 | 2.2512924103616968e-06 | 5.71% | 6.06% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3349184473537485e-06 | 2.1312696472413315e-06 | 8.72% | 9.56% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 3.095272590384024e-06 | 2.845198944551575e-06 | 8.08% | 8.79% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.0995650969923287e-06 | 2.8336841685375845e-06 | 8.58% | 9.38% | 1.09x | ✅ |
