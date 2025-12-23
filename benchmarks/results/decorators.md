#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1803120106493221e-05 | 2.2302293445610104e-05 | -88.95% | -47.08% | 0.53x | ❌ |
| `replace_exceptions[no-exception]` | 1.4348526157658014e-06 | 1.3808307874897576e-06 | 3.76% | 3.91% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.363215441286887e-06 | 1.3531358628879689e-05 | -61.80% | -38.19% | 0.62x | ❌ |
| `return_arg_type[float-pos0]` | 2.3124487477743296e-06 | 2.0829561955976383e-06 | 9.92% | 11.02% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.2157739311838553e-06 | 2.0977655875964466e-06 | 5.33% | 5.63% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.102639275691632e-06 | 1.966309813129718e-06 | 6.48% | 6.93% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 2.869213622021679e-06 | 2.7192896965822177e-06 | 5.23% | 5.51% | 1.06x | ✅ |
| `return_arg_type[str-pos1]` | 2.90002283348354e-06 | 2.7149522084163744e-06 | 6.38% | 6.82% | 1.07x | ✅ |
