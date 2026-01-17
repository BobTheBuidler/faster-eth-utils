#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1970814570833374e-05 | 2.4367698203426453e-05 | -103.56% | -50.87% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6202990175751365e-06 | 1.4524916181468937e-06 | 10.36% | 11.55% | 1.12x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.429897510010024e-06 | 1.4652498075938566e-05 | -73.82% | -42.47% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4817179992894253e-06 | 2.3689465679915143e-06 | 4.54% | 4.76% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.4543052806989094e-06 | 2.2497273137851734e-06 | 8.34% | 9.09% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.3523616375137507e-06 | 2.17345190708055e-06 | 7.61% | 8.23% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.1539190764893544e-06 | 2.9423018332518275e-06 | 6.71% | 7.19% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 3.0644473915483627e-06 | 2.9159964894114615e-06 | 4.84% | 5.09% | 1.05x | ✅ |
