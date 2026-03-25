#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1633657845931062e-05 | 2.417513354958447e-05 | -107.80% | -51.88% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5196327972369652e-06 | 1.524831135019699e-06 | -0.34% | -0.34% | 1.00x | ❌ |
| `replace_exceptions[unmapped-exception]` | 8.355757975238988e-06 | 1.4523926905102251e-05 | -73.82% | -42.47% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.37837838290987e-06 | 2.1658941306118906e-06 | 8.93% | 9.81% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.3538973514783456e-06 | 2.1318849463530375e-06 | 9.43% | 10.41% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.2965495001058884e-06 | 2.103863805837996e-06 | 8.39% | 9.16% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 2.86405106757145e-06 | 2.783485893930022e-06 | 2.81% | 2.89% | 1.03x | ✅ |
| `return_arg_type[str-pos1]` | 2.891956694285596e-06 | 2.7675164547109884e-06 | 4.30% | 4.50% | 1.04x | ✅ |
