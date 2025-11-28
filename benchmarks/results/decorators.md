#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1812080384991281e-05 | 2.4083250175380418e-05 | -103.89% | -50.95% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5431411990411388e-06 | 1.4180288299865641e-06 | 8.11% | 8.82% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.43279099209247e-06 | 1.449975194040031e-05 | -71.94% | -41.84% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.3676208178165538e-06 | 2.07755837744393e-06 | 12.25% | 13.96% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.3062980617174965e-06 | 2.1216727691460655e-06 | 8.01% | 8.70% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.281555237363305e-06 | 2.0049178847538374e-06 | 12.12% | 13.80% | 1.14x | ✅ |
| `return_arg_type[str-pos0]` | 2.892749319806846e-06 | 2.7812586912465918e-06 | 3.85% | 4.01% | 1.04x | ✅ |
| `return_arg_type[str-pos1]` | 2.898905136357604e-06 | 2.7715629031500198e-06 | 4.39% | 4.59% | 1.05x | ✅ |
