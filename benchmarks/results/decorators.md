#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2082709447210377e-05 | 2.54835229611259e-05 | -110.91% | -52.59% | 0.47x | ❌ |
| `replace_exceptions[no-exception]` | 1.579271892719713e-06 | 1.5098732859792253e-06 | 4.39% | 4.60% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.571200736752036e-06 | 1.4910104376581474e-05 | -73.96% | -42.51% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.468264398200068e-06 | 2.3290293749067116e-06 | 5.64% | 5.98% | 1.06x | ✅ |
| `return_arg_type[int-pos0]` | 2.401583506547286e-06 | 2.2901403706147126e-06 | 4.64% | 4.87% | 1.05x | ✅ |
| `return_arg_type[int-pos1]` | 2.396323822429158e-06 | 2.1791669890284063e-06 | 9.06% | 9.97% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 3.0882285639714658e-06 | 3.1341594935238627e-06 | -1.49% | -1.47% | 0.99x | ❌ |
| `return_arg_type[str-pos1]` | 3.1375294757988994e-06 | 3.0022611524797478e-06 | 4.31% | 4.51% | 1.05x | ✅ |
