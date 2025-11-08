#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.170199411777128e-05 | 2.3780737728367194e-05 | -103.22% | -50.79% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5156234835208212e-06 | 1.4424667650117136e-06 | 4.83% | 5.07% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.486505312713932e-06 | 1.4381404999370998e-05 | -69.46% | -40.99% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.334116187849056e-06 | 2.0496333667497753e-06 | 12.19% | 13.88% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.300857530086268e-06 | 2.054496239605258e-06 | 10.71% | 11.99% | 1.12x | ✅ |
| `return_arg_type[int-pos1]` | 2.27056562826666e-06 | 1.969376950569965e-06 | 13.26% | 15.29% | 1.15x | ✅ |
| `return_arg_type[str-pos0]` | 2.865213974027442e-06 | 2.7061476520669786e-06 | 5.55% | 5.88% | 1.06x | ✅ |
| `return_arg_type[str-pos1]` | 2.9419400456702517e-06 | 2.706052734828966e-06 | 8.02% | 8.72% | 1.09x | ✅ |
