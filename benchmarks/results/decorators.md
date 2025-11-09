#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1704246563504124e-05 | 2.4311501798604745e-05 | -107.72% | -51.86% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5300213006968948e-06 | 1.4179852296369668e-06 | 7.32% | 7.90% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.454088716398586e-06 | 1.4812445020111151e-05 | -75.21% | -42.93% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.3856598529483465e-06 | 2.1965747208481197e-06 | 7.93% | 8.61% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.3847933550045902e-06 | 2.0964424393512703e-06 | 12.09% | 13.75% | 1.14x | ✅ |
| `return_arg_type[int-pos1]` | 2.333500498477706e-06 | 2.0257709083555807e-06 | 13.19% | 15.19% | 1.15x | ✅ |
| `return_arg_type[str-pos0]` | 2.9246966684369986e-06 | 2.7353710865587936e-06 | 6.47% | 6.92% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.9485618666150403e-06 | 2.8017124937056417e-06 | 4.98% | 5.24% | 1.05x | ✅ |
