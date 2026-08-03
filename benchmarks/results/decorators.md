#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1758328646393702e-05 | 2.4075080033885913e-05 | -104.75% | -51.16% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5930822128830756e-06 | 1.4487274625598465e-06 | 9.06% | 9.96% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.408450046710771e-06 | 1.4619078855691998e-05 | -73.86% | -42.48% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4447563157410673e-06 | 2.1391330058164103e-06 | 12.50% | 14.29% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.3001382608765636e-06 | 2.116297928416014e-06 | 7.99% | 8.69% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.268414875556448e-06 | 1.997470865244536e-06 | 11.94% | 13.56% | 1.14x | ✅ |
| `return_arg_type[str-pos0]` | 2.752989537483578e-06 | 2.5816463539320716e-06 | 6.22% | 6.64% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.815865684630661e-06 | 2.600495601094517e-06 | 7.65% | 8.28% | 1.08x | ✅ |
