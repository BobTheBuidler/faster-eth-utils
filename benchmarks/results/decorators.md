#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2774793273743314e-05 | 2.5605140239025165e-05 | -100.43% | -50.11% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.5257169426288314e-06 | 1.5093336193485526e-06 | 1.07% | 1.09% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.881392950634136e-06 | 1.5137494542679683e-05 | -70.44% | -41.33% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.3914399745976906e-06 | 2.2734570632793156e-06 | 4.93% | 5.19% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.4848592539454027e-06 | 2.2838538442453115e-06 | 8.09% | 8.80% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.3902923304161703e-06 | 2.1884830822686133e-06 | 8.44% | 9.22% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 2.98844504456136e-06 | 2.997553126392483e-06 | -0.30% | -0.30% | 1.00x | ❌ |
| `return_arg_type[str-pos1]` | 2.9825830386126743e-06 | 2.909429701918301e-06 | 2.45% | 2.51% | 1.03x | ✅ |
