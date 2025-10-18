#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2202351640438077e-05 | 2.2406666806981744e-05 | -83.63% | -45.54% | 0.54x | ❌ |
| `replace_exceptions[no-exception]` | 1.5577376602961229e-06 | 1.4900854913853696e-06 | 4.34% | 4.54% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.454115022674091e-06 | 1.3984515141051239e-05 | -65.42% | -39.55% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.592725027971703e-06 | 2.3186699587660862e-06 | 10.57% | 11.82% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.9611073711230384e-06 | 2.6171154965366786e-06 | 11.62% | 13.14% | 1.13x | ✅ |
| `return_arg_type[int-pos1]` | 2.9046409451191846e-06 | 2.6215705074681478e-06 | 9.75% | 10.80% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 2.904596548180859e-06 | 3.1117528452769873e-06 | -7.13% | -6.66% | 0.93x | ❌ |
| `return_arg_type[str-pos1]` | 2.8215457135567837e-06 | 3.1445944096225784e-06 | -11.45% | -10.27% | 0.90x | ❌ |
