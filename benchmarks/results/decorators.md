#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1766057384402094e-05 | 2.4338835033958053e-05 | -106.86% | -51.66% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.570510170775637e-06 | 1.4563391276040892e-06 | 7.27% | 7.84% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.687037774979229e-06 | 1.4693366185625328e-05 | -69.14% | -40.88% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4278345868930185e-06 | 2.1489490937198103e-06 | 11.49% | 12.98% | 1.13x | ✅ |
| `return_arg_type[int-pos0]` | 2.3339812422869023e-06 | 2.1127059397367177e-06 | 9.48% | 10.47% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.3147359371454367e-06 | 2.0321773038107055e-06 | 12.21% | 13.90% | 1.14x | ✅ |
| `return_arg_type[str-pos0]` | 2.9841109363844257e-06 | 2.7573008519387527e-06 | 7.60% | 8.23% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 2.997777137447831e-06 | 2.8107177131108726e-06 | 6.24% | 6.66% | 1.07x | ✅ |
