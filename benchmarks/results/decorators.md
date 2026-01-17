#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1889947367404208e-05 | 2.4466464606160926e-05 | -105.77% | -51.40% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6295295146629273e-06 | 1.4682901174508731e-06 | 9.89% | 10.98% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.362036314942592e-06 | 1.464104735176655e-05 | -75.09% | -42.89% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4967592069726996e-06 | 2.3010179759463062e-06 | 7.84% | 8.51% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.4190700808144922e-06 | 2.298006559540493e-06 | 5.00% | 5.27% | 1.05x | ✅ |
| `return_arg_type[int-pos1]` | 2.340004270271813e-06 | 2.169436982851093e-06 | 7.29% | 7.86% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.0437637394588164e-06 | 2.856516107962242e-06 | 6.15% | 6.56% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 3.050367601782237e-06 | 2.9236460143232296e-06 | 4.15% | 4.33% | 1.04x | ✅ |
