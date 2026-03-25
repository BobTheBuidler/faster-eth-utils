#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1691814309463811e-05 | 2.4221538938728e-05 | -107.17% | -51.73% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5431471991994925e-06 | 1.5150027035730835e-06 | 1.82% | 1.86% | 1.02x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.332435419287717e-06 | 1.4856461533314269e-05 | -78.30% | -43.91% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.398384746546136e-06 | 2.168639048187999e-06 | 9.58% | 10.59% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.3144345187630597e-06 | 2.1619034721551513e-06 | 6.59% | 7.06% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.2581429188318237e-06 | 2.0560389623413555e-06 | 8.95% | 9.83% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.9242764732186673e-06 | 2.7371572019176584e-06 | 6.40% | 6.84% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.914164782181766e-06 | 2.7448784265975352e-06 | 5.81% | 6.17% | 1.06x | ✅ |
