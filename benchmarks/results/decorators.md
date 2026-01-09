#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1923552972149216e-05 | 2.4842738129267547e-05 | -108.35% | -52.00% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6275975795955576e-06 | 1.4799184255767183e-06 | 9.07% | 9.98% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.44613812774724e-06 | 1.4914363300825402e-05 | -76.58% | -43.37% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4467640951340725e-06 | 2.2865617871984135e-06 | 6.55% | 7.01% | 1.07x | ✅ |
| `return_arg_type[int-pos0]` | 2.3861776110204676e-06 | 2.2505081232758607e-06 | 5.69% | 6.03% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3042275255212536e-06 | 2.19363214963681e-06 | 4.80% | 5.04% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.1798915563440285e-06 | 2.9086604234497532e-06 | 8.53% | 9.32% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.0499162356441295e-06 | 2.8687952897754795e-06 | 5.94% | 6.31% | 1.06x | ✅ |
