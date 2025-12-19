#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.184806510435821e-05 | 2.389059553546071e-05 | -101.64% | -50.41% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.5695218408141109e-06 | 1.4689299789081702e-06 | 6.41% | 6.85% | 1.07x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.333514001030255e-06 | 1.4383982274658415e-05 | -72.60% | -42.06% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.444927157700214e-06 | 2.3667403863377644e-06 | 3.20% | 3.30% | 1.03x | ✅ |
| `return_arg_type[int-pos0]` | 2.3359890787800904e-06 | 2.2518978812522712e-06 | 3.60% | 3.73% | 1.04x | ✅ |
| `return_arg_type[int-pos1]` | 2.2522771360647486e-06 | 2.1631752267000452e-06 | 3.96% | 4.12% | 1.04x | ✅ |
| `return_arg_type[str-pos0]` | 3.145585784739236e-06 | 2.784992852097958e-06 | 11.46% | 12.95% | 1.13x | ✅ |
| `return_arg_type[str-pos1]` | 3.110979126889399e-06 | 2.7676741560387412e-06 | 11.04% | 12.40% | 1.12x | ✅ |
