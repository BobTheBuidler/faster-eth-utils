#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1755470729587752e-05 | 2.44108523493641e-05 | -107.66% | -51.84% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5393543211847347e-06 | 1.531201762743119e-06 | 0.53% | 0.53% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.498798443733072e-06 | 1.4683862331682865e-05 | -72.78% | -42.12% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.500324219079377e-06 | 2.2652845959606644e-06 | 9.40% | 10.38% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.365593696673129e-06 | 2.1749689459302288e-06 | 8.06% | 8.76% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.35822508803795e-06 | 2.036237763172672e-06 | 13.65% | 15.81% | 1.16x | ✅ |
| `return_arg_type[str-pos0]` | 3.0029430459066135e-06 | 2.810324716202999e-06 | 6.41% | 6.85% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.939893445093458e-06 | 2.8261154097166045e-06 | 3.87% | 4.03% | 1.04x | ✅ |
