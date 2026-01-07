#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1847369498631272e-05 | 2.4033312456867365e-05 | -102.86% | -50.70% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5718683479428023e-06 | 1.487738115529458e-06 | 5.35% | 5.65% | 1.06x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.55609170128852e-06 | 1.4439132720451762e-05 | -68.76% | -40.74% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4872737799026285e-06 | 2.35140859843967e-06 | 5.46% | 5.78% | 1.06x | ✅ |
| `return_arg_type[int-pos0]` | 2.3876904894085754e-06 | 2.2506880383466604e-06 | 5.74% | 6.09% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3434976068774356e-06 | 2.185566643095641e-06 | 6.74% | 7.23% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 3.131554634325217e-06 | 2.8391359841159094e-06 | 9.34% | 10.30% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 3.032261272439504e-06 | 2.7728185570360656e-06 | 8.56% | 9.36% | 1.09x | ✅ |
