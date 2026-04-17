#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1796558252289261e-05 | 2.4691875342788662e-05 | -109.31% | -52.22% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.4869332314498042e-06 | 1.445524219644201e-06 | 2.78% | 2.86% | 1.03x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.533735020193194e-06 | 1.4801292546409145e-05 | -73.44% | -42.34% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.3831952875274392e-06 | 2.2647195930259467e-06 | 4.97% | 5.23% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.3720074542813827e-06 | 2.2148429736045087e-06 | 6.63% | 7.10% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.280051499138518e-06 | 2.1416406544800147e-06 | 6.07% | 6.46% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 2.9528379022519584e-06 | 2.7504574148373015e-06 | 6.85% | 7.36% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.898118180606732e-06 | 2.7227969708736055e-06 | 6.05% | 6.44% | 1.06x | ✅ |
