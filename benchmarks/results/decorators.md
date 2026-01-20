#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2518987515561705e-05 | 2.4274339101632206e-05 | -93.90% | -48.43% | 0.52x | ❌ |
| `replace_exceptions[no-exception]` | 1.6716275940853713e-06 | 1.485240873585933e-06 | 11.15% | 12.55% | 1.13x | ✅ |
| `replace_exceptions[unmapped-exception]` | 9.186573458334453e-06 | 1.4898668467846117e-05 | -62.18% | -38.34% | 0.62x | ❌ |
| `return_arg_type[float-pos0]` | 2.4956879007915542e-06 | 2.296577142439773e-06 | 7.98% | 8.67% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.3568105340365583e-06 | 2.2688021042822875e-06 | 3.73% | 3.88% | 1.04x | ✅ |
| `return_arg_type[int-pos1]` | 2.291045360669995e-06 | 2.1788027059992115e-06 | 4.90% | 5.15% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.041101432883041e-06 | 2.929240246124445e-06 | 3.68% | 3.82% | 1.04x | ✅ |
| `return_arg_type[str-pos1]` | 3.030327027834991e-06 | 2.847277087653752e-06 | 6.04% | 6.43% | 1.06x | ✅ |
