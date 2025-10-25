#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.255817863243131e-05 | 2.220120798828985e-05 | -76.79% | -43.43% | 0.57x | ❌ |
| `replace_exceptions[no-exception]` | 1.5528125027014047e-06 | 1.4226489392214169e-06 | 8.38% | 9.15% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.809365676669576e-06 | 1.3567356398641292e-05 | -54.01% | -35.07% | 0.65x | ❌ |
| `return_arg_type[float-pos0]` | 2.577491861195484e-06 | 2.1932203970645183e-06 | 14.91% | 17.52% | 1.18x | ✅ |
| `return_arg_type[int-pos0]` | 2.9167285978139616e-06 | 2.564960609144319e-06 | 12.06% | 13.71% | 1.14x | ✅ |
| `return_arg_type[int-pos1]` | 2.87565423765611e-06 | 2.5582000146543518e-06 | 11.04% | 12.41% | 1.12x | ✅ |
| `return_arg_type[str-pos0]` | 3.007337080277684e-06 | 3.21085308296866e-06 | -6.77% | -6.34% | 0.94x | ❌ |
| `return_arg_type[str-pos1]` | 2.9786019267312204e-06 | 3.1933827775233345e-06 | -7.21% | -6.73% | 0.93x | ❌ |
