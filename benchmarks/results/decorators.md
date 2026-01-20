#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1967253549819384e-05 | 2.4482032285411703e-05 | -104.58% | -51.12% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6367903741045255e-06 | 1.50925409655372e-06 | 7.79% | 8.45% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.643109606976883e-06 | 1.4616872877543725e-05 | -69.12% | -40.87% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4714556996537467e-06 | 2.2978469202643007e-06 | 7.02% | 7.56% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.405186614414529e-06 | 2.259782721030415e-06 | 6.05% | 6.43% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.315605886590417e-06 | 2.1560965466889338e-06 | 6.89% | 7.40% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 3.048935047910173e-06 | 2.9032365038024946e-06 | 4.78% | 5.02% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 3.060090775321197e-06 | 2.8302653890999808e-06 | 7.51% | 8.12% | 1.08x | ✅ |
