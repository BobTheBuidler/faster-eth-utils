#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.128638157798669e-05 | 2.2862119707152657e-05 | -102.56% | -50.63% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.3603251163561845e-06 | 1.321165289875141e-06 | 2.88% | 2.96% | 1.03x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.286618797143415e-06 | 1.3334522399468035e-05 | -60.92% | -37.86% | 0.62x | ❌ |
| `return_arg_type[float-pos0]` | 2.1978464418680827e-06 | 1.993277669155014e-06 | 9.31% | 10.26% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.1951833631015746e-06 | 1.9900503703412895e-06 | 9.34% | 10.31% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.1072570902747895e-06 | 1.8883222145833678e-06 | 10.39% | 11.59% | 1.12x | ✅ |
| `return_arg_type[str-pos0]` | 2.7359418322803807e-06 | 2.5239484006627727e-06 | 7.75% | 8.40% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 2.7453885709955524e-06 | 2.5252743633305987e-06 | 8.02% | 8.72% | 1.09x | ✅ |
