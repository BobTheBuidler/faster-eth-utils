#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.175188521792837e-05 | 2.45178515811401e-05 | -108.63% | -52.07% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5813399264061629e-06 | 1.441990965187845e-06 | 8.81% | 9.66% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.649548168764886e-06 | 1.4790679979827327e-05 | -71.00% | -41.52% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.444595744672705e-06 | 2.151069749129778e-06 | 12.01% | 13.65% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.282833564817126e-06 | 2.0997571890997765e-06 | 8.02% | 8.72% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.2298775018130975e-06 | 2.0431217934809234e-06 | 8.38% | 9.14% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 2.8845276725226846e-06 | 2.7378220961043836e-06 | 5.09% | 5.36% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 2.8939614255020994e-06 | 2.718641488107414e-06 | 6.06% | 6.45% | 1.06x | ✅ |
