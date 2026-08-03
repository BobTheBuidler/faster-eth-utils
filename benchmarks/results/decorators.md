#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2800763870233928e-05 | 2.5248907841567e-05 | -97.25% | -49.30% | 0.51x | ❌ |
| `replace_exceptions[no-exception]` | 1.5465510096168873e-06 | 1.5271096196724118e-06 | 1.26% | 1.27% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.936907593123764e-06 | 1.524917577301521e-05 | -70.63% | -41.39% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4164831481691257e-06 | 2.321203685987249e-06 | 3.94% | 4.10% | 1.04x | ✅ |
| `return_arg_type[int-pos0]` | 2.4805008585917624e-06 | 2.4175357072151783e-06 | 2.54% | 2.60% | 1.03x | ✅ |
| `return_arg_type[int-pos1]` | 2.414013880636126e-06 | 2.33708819479536e-06 | 3.19% | 3.29% | 1.03x | ✅ |
| `return_arg_type[str-pos0]` | 2.9919397432428346e-06 | 2.9941858685930417e-06 | -0.08% | -0.08% | 1.00x | ❌ |
| `return_arg_type[str-pos1]` | 3.050667789743779e-06 | 2.9121112810640655e-06 | 4.54% | 4.76% | 1.05x | ✅ |
