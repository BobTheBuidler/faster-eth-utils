#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1928029420443343e-05 | 2.4960194794195404e-05 | -109.26% | -52.21% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5516562102512707e-06 | 1.436848949670665e-06 | 7.40% | 7.99% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.748363697653152e-06 | 1.5073838718939223e-05 | -72.30% | -41.96% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4413383307136987e-06 | 2.1578907753436123e-06 | 11.61% | 13.14% | 1.13x | ✅ |
| `return_arg_type[int-pos0]` | 2.394001644818958e-06 | 2.1034533663668363e-06 | 12.14% | 13.81% | 1.14x | ✅ |
| `return_arg_type[int-pos1]` | 2.340496555541642e-06 | 2.0331302140878303e-06 | 13.13% | 15.12% | 1.15x | ✅ |
| `return_arg_type[str-pos0]` | 2.9909179651954536e-06 | 2.775705740125137e-06 | 7.20% | 7.75% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 2.938191405774311e-06 | 2.7896308521778274e-06 | 5.06% | 5.33% | 1.05x | ✅ |
