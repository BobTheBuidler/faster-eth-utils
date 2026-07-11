#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1716968802798758e-05 | 2.4277421605870365e-05 | -107.20% | -51.74% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5717672389845497e-06 | 1.4267676458097022e-06 | 9.23% | 10.16% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.388338100132528e-06 | 1.4695359408134433e-05 | -75.19% | -42.92% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.37234154711285e-06 | 2.06381913618432e-06 | 13.00% | 14.95% | 1.15x | ✅ |
| `return_arg_type[int-pos0]` | 2.2250622796085463e-06 | 2.0263817874759036e-06 | 8.93% | 9.80% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.1827270276327033e-06 | 2.042086078931827e-06 | 6.44% | 6.89% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 2.760145262002814e-06 | 2.575748452737218e-06 | 6.68% | 7.16% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.7515680571766823e-06 | 2.582793732666103e-06 | 6.13% | 6.53% | 1.07x | ✅ |
