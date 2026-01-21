#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1838381071893153e-05 | 2.4009165598970964e-05 | -102.81% | -50.69% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.585108643670772e-06 | 1.4668249705185614e-06 | 7.46% | 8.06% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.33049927386223e-06 | 1.3992536939883256e-05 | -67.97% | -40.46% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.523256231226924e-06 | 2.2471285577348275e-06 | 10.94% | 12.29% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.2672542965733275e-06 | 2.228469284185135e-06 | 1.71% | 1.74% | 1.02x | ✅ |
| `return_arg_type[int-pos1]` | 2.2247040107656826e-06 | 2.1163652748024885e-06 | 4.87% | 5.12% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.192854833025742e-06 | 2.7440612128935207e-06 | 14.06% | 16.36% | 1.16x | ✅ |
| `return_arg_type[str-pos1]` | 3.033654882091633e-06 | 2.7716972884463114e-06 | 8.64% | 9.45% | 1.09x | ✅ |
