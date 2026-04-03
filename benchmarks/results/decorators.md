#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1812422146068734e-05 | 2.4163266188919247e-05 | -104.56% | -51.11% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5322745153436732e-06 | 1.4794620840272555e-06 | 3.45% | 3.57% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.506227421369767e-06 | 1.4561707387528155e-05 | -71.19% | -41.58% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.41339969826808e-06 | 2.2272726916733387e-06 | 7.71% | 8.36% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.302640653292351e-06 | 2.166234262157827e-06 | 5.92% | 6.30% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.2904645794405824e-06 | 2.079656870563922e-06 | 9.20% | 10.14% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.9041282429323055e-06 | 2.7235882662128954e-06 | 6.22% | 6.63% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.887502193975232e-06 | 2.654240225814628e-06 | 8.08% | 8.79% | 1.09x | ✅ |
