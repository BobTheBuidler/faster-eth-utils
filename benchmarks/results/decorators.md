#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.181034687644423e-05 | 2.409393581143306e-05 | -104.01% | -50.98% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5676205450528527e-06 | 1.4467184797923238e-06 | 7.71% | 8.36% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.477279218109503e-06 | 1.4489358972645356e-05 | -70.92% | -41.49% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4027799408061e-06 | 2.192837722234068e-06 | 8.74% | 9.57% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.259859771092736e-06 | 2.1284871486271055e-06 | 5.81% | 6.17% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.280175595890433e-06 | 2.080982655092067e-06 | 8.74% | 9.57% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.889332939988019e-06 | 2.821596065535405e-06 | 2.34% | 2.40% | 1.02x | ✅ |
| `return_arg_type[str-pos1]` | 2.8878515152750196e-06 | 2.7646955194483256e-06 | 4.26% | 4.45% | 1.04x | ✅ |
