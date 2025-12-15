#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1703489958392925e-05 | 2.2963871272550828e-05 | -96.21% | -49.04% | 0.51x | ❌ |
| `replace_exceptions[no-exception]` | 1.4471070696528894e-06 | 1.6074686755179713e-06 | -11.08% | -9.98% | 0.90x | ❌ |
| `replace_exceptions[unmapped-exception]` | 8.246033726961594e-06 | 1.3647604021402663e-05 | -65.51% | -39.58% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.2666186865959815e-06 | 2.153255845511807e-06 | 5.00% | 5.26% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.1343675802687267e-06 | 2.0174879621389154e-06 | 5.48% | 5.79% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.0933745866356513e-06 | 2.001184252047415e-06 | 4.40% | 4.61% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 2.835236236814695e-06 | 2.7911548644972014e-06 | 1.55% | 1.58% | 1.02x | ✅ |
| `return_arg_type[str-pos1]` | 2.8511616066599007e-06 | 2.93878199281432e-06 | -3.07% | -2.98% | 0.97x | ❌ |
