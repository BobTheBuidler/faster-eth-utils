#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1797250968319632e-05 | 2.4419539226994017e-05 | -106.99% | -51.69% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6361762722496312e-06 | 1.4679848863575466e-06 | 10.28% | 11.46% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.395035068853571e-06 | 1.4515866961858089e-05 | -72.91% | -42.17% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.482706405700768e-06 | 2.282239149909927e-06 | 8.07% | 8.78% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.449428217742997e-06 | 2.2677555557122776e-06 | 7.42% | 8.01% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.332061278422563e-06 | 2.165922998148948e-06 | 7.12% | 7.67% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.1657482394014574e-06 | 2.911686195402492e-06 | 8.03% | 8.73% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.0908170745684557e-06 | 2.844487646076712e-06 | 7.97% | 8.66% | 1.09x | ✅ |
