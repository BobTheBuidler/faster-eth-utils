#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1970083377569786e-05 | 2.3928589777233865e-05 | -99.90% | -49.98% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.6337011178769544e-06 | 1.5083293101165473e-06 | 7.67% | 8.31% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.513583978201672e-06 | 1.430018704397238e-05 | -67.97% | -40.47% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.4687183742180734e-06 | 2.294964836726022e-06 | 7.04% | 7.57% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.449701194361637e-06 | 2.2797701285771736e-06 | 6.94% | 7.45% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.344518294308126e-06 | 2.1626450671484154e-06 | 7.76% | 8.41% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.215230546138937e-06 | 2.8514094077184862e-06 | 11.32% | 12.76% | 1.13x | ✅ |
| `return_arg_type[str-pos1]` | 3.0747486867265334e-06 | 2.8425950939483694e-06 | 7.55% | 8.17% | 1.08x | ✅ |
