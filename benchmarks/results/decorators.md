#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1731092424329497e-05 | 2.462723319615109e-05 | -109.93% | -52.37% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.661422468840541e-06 | 1.5927192798484303e-06 | 4.14% | 4.31% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.391762111475302e-06 | 1.4682042220114038e-05 | -74.96% | -42.84% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4832926966227443e-06 | 2.3029302649127044e-06 | 7.26% | 7.83% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.3272807323718997e-06 | 2.1689421308237957e-06 | 6.80% | 7.30% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.277928443250646e-06 | 2.0766998986722983e-06 | 8.83% | 9.69% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.9806205247011474e-06 | 2.8324549883664897e-06 | 4.97% | 5.23% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 2.9476209457635435e-06 | 2.829062126171346e-06 | 4.02% | 4.19% | 1.04x | ✅ |
