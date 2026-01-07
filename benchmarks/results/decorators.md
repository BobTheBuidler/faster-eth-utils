#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.139393679082312e-05 | 2.3219200431757467e-05 | -103.79% | -50.93% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.4304495812559658e-06 | 1.4192419875623116e-06 | 0.78% | 0.79% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.389668988286726e-06 | 1.386422091274634e-05 | -65.25% | -39.49% | 0.61x | ❌ |
| `return_arg_type[float-pos0]` | 2.235997809663967e-06 | 2.0222154219103836e-06 | 9.56% | 10.57% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.20701383625463e-06 | 2.0524278758029784e-06 | 7.00% | 7.53% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.0752213957643996e-06 | 1.9501693323625777e-06 | 6.03% | 6.41% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 2.8774360774894085e-06 | 2.669726318661084e-06 | 7.22% | 7.78% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 2.876886542796695e-06 | 2.6620733703536723e-06 | 7.47% | 8.07% | 1.08x | ✅ |
