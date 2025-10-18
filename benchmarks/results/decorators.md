#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.169211139388903e-05 | 2.452448226732889e-05 | -109.75% | -52.32% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.487502750378822e-06 | 1.442303427119104e-06 | 3.04% | 3.13% | 1.03x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.532294867679165e-06 | 1.4477620204769263e-05 | -69.68% | -41.07% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.3852712077906046e-06 | 2.1458382441955825e-06 | 10.04% | 11.16% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.3406392274818438e-06 | 2.1085362576378577e-06 | 9.92% | 11.01% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.250905837018184e-06 | 2.0267694306520494e-06 | 9.96% | 11.06% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 2.910599921737391e-06 | 2.8574832423822572e-06 | 1.82% | 1.86% | 1.02x | ✅ |
| `return_arg_type[str-pos1]` | 2.904864734092387e-06 | 2.790852686945544e-06 | 3.92% | 4.09% | 1.04x | ✅ |
