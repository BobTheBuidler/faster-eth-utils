#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1570270549225729e-05 | 2.4039050121930862e-05 | -107.77% | -51.87% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5723814284388267e-06 | 1.5541333110524592e-06 | 1.16% | 1.17% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.131257420672485e-06 | 1.4326426056119258e-05 | -76.19% | -43.24% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4364274050180133e-06 | 2.096515499747728e-06 | 13.95% | 16.21% | 1.16x | ✅ |
| `return_arg_type[int-pos0]` | 2.3712800071189294e-06 | 2.0753767520938945e-06 | 12.48% | 14.26% | 1.14x | ✅ |
| `return_arg_type[int-pos1]` | 2.31818888434631e-06 | 1.9857289518213606e-06 | 14.34% | 16.74% | 1.17x | ✅ |
| `return_arg_type[str-pos0]` | 2.892833202387197e-06 | 2.6252483171808937e-06 | 9.25% | 10.19% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 2.8211060210053974e-06 | 2.5246647162433683e-06 | 10.51% | 11.74% | 1.12x | ✅ |
