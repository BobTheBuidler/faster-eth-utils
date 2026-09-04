#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.0787228185537999e-05 | 2.1361332163965937e-05 | -98.02% | -49.50% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.3248823640298325e-06 | 1.2194694709976775e-06 | 7.96% | 8.64% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 7.798159845154264e-06 | 1.2444110831880265e-05 | -59.58% | -37.33% | 0.63x | ❌ |
| `return_arg_type[float-pos0]` | 2.028692121720119e-06 | 1.882001322300515e-06 | 7.23% | 7.79% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.013125178875898e-06 | 1.8471806553462045e-06 | 8.24% | 8.98% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 1.9495442421570487e-06 | 1.7779658626180082e-06 | 8.80% | 9.65% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.469844005946537e-06 | 2.322442183130875e-06 | 5.97% | 6.35% | 1.06x | ✅ |
| `return_arg_type[str-pos1]` | 2.434530338329761e-06 | 2.2750339654999863e-06 | 6.55% | 7.01% | 1.07x | ✅ |
