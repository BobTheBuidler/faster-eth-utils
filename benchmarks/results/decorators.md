#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2191521285571992e-05 | 2.4206408656914418e-05 | -98.55% | -49.64% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.6512121115735188e-06 | 1.494767127292561e-06 | 9.47% | 10.47% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.572339338884512e-06 | 1.4385343415809208e-05 | -67.81% | -40.41% | 0.60x | ❌ |
| `return_arg_type[float-pos0]` | 2.6250192242201364e-06 | 2.3560428672419784e-06 | 10.25% | 11.42% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.4727084141939675e-06 | 2.336148492583975e-06 | 5.52% | 5.85% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.43767623988503e-06 | 2.2300422124131416e-06 | 8.52% | 9.31% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 3.112172461248569e-06 | 2.8583336202717563e-06 | 8.16% | 8.88% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.0787511242433714e-06 | 2.9361490029110985e-06 | 4.63% | 4.86% | 1.05x | ✅ |
