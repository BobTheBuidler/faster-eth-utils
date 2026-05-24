#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2251223687348577e-05 | 2.650778274876213e-05 | -116.37% | -53.78% | 0.46x | ❌ |
| `replace_exceptions[no-exception]` | 1.5464295133335912e-06 | 1.5250090329796103e-06 | 1.39% | 1.40% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.799980835868264e-06 | 1.5362634012903582e-05 | -74.58% | -42.72% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4257146742650527e-06 | 2.2186800247800585e-06 | 8.53% | 9.33% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.4027837615388993e-06 | 2.167513089635171e-06 | 9.79% | 10.85% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.3219892985914415e-06 | 2.0745432836000667e-06 | 10.66% | 11.93% | 1.12x | ✅ |
| `return_arg_type[str-pos0]` | 2.82157395200253e-06 | 2.7294189997303707e-06 | 3.27% | 3.38% | 1.03x | ✅ |
| `return_arg_type[str-pos1]` | 2.825993284921742e-06 | 2.724569652733917e-06 | 3.59% | 3.72% | 1.04x | ✅ |
