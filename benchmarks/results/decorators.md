#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2302141540368928e-05 | 2.5080090944252187e-05 | -103.87% | -50.95% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6964292076953056e-06 | 1.5223428406504641e-06 | 10.26% | 11.44% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.874560031280942e-06 | 1.4675589910442512e-05 | -65.37% | -39.53% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.5567313467716195e-06 | 2.2196515272627807e-06 | 13.18% | 15.19% | 1.15x | ✅ |
| `return_arg_type[int-pos0]` | 2.476943234691419e-06 | 2.1907343986011783e-06 | 11.55% | 13.06% | 1.13x | ✅ |
| `return_arg_type[int-pos1]` | 2.4195600902267435e-06 | 2.090882146337517e-06 | 13.58% | 15.72% | 1.16x | ✅ |
| `return_arg_type[str-pos0]` | 3.155864957409367e-06 | 2.8675534030924104e-06 | 9.14% | 10.05% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 3.0633615395084037e-06 | 2.8653918967104103e-06 | 6.46% | 6.91% | 1.07x | ✅ |
