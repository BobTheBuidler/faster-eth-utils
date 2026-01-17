#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.184701951206564e-05 | 2.417711585094571e-05 | -104.08% | -51.00% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.60391584548264e-06 | 1.486975380494916e-06 | 7.29% | 7.86% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.322801278873704e-06 | 1.4240014562218906e-05 | -71.10% | -41.55% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.461389505606173e-06 | 2.308787353625676e-06 | 6.20% | 6.61% | 1.07x | ✅ |
| `return_arg_type[int-pos0]` | 2.366697625707125e-06 | 2.229887838396628e-06 | 5.78% | 6.14% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.281595927386823e-06 | 2.1630951745832315e-06 | 5.19% | 5.48% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.0642654420104522e-06 | 2.964644205270632e-06 | 3.25% | 3.36% | 1.03x | ✅ |
| `return_arg_type[str-pos1]` | 3.098042462001563e-06 | 2.8732461617083355e-06 | 7.26% | 7.82% | 1.08x | ✅ |
