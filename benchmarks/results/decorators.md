#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1682014552106852e-05 | 2.3878328085537366e-05 | -104.40% | -51.08% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5419599108967784e-06 | 1.472272000374132e-06 | 4.52% | 4.73% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.472217270198221e-06 | 1.4667341401604114e-05 | -73.12% | -42.24% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.3597292696776207e-06 | 2.1119668057822794e-06 | 10.50% | 11.73% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.320303067559773e-06 | 2.102242578714353e-06 | 9.40% | 10.37% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.260210513319933e-06 | 1.999050597186362e-06 | 11.55% | 13.06% | 1.13x | ✅ |
| `return_arg_type[str-pos0]` | 2.8693751826806494e-06 | 2.7351444008109646e-06 | 4.68% | 4.91% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 2.918669573413393e-06 | 2.7411990668853573e-06 | 6.08% | 6.47% | 1.06x | ✅ |
