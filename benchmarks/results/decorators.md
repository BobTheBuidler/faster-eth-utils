#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1829474418032438e-05 | 2.4252713110321045e-05 | -105.02% | -51.22% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6291964667274028e-06 | 1.5180023935131806e-06 | 6.83% | 7.33% | 1.07x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.338729958099193e-06 | 1.4354742301141061e-05 | -72.15% | -41.91% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.478426090137977e-06 | 2.2972482044261894e-06 | 7.31% | 7.89% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.492979451949871e-06 | 2.305561857007164e-06 | 7.52% | 8.13% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.321548976191143e-06 | 2.176001204269982e-06 | 6.27% | 6.69% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 3.108534378459987e-06 | 2.9223766182231973e-06 | 5.99% | 6.37% | 1.06x | ✅ |
| `return_arg_type[str-pos1]` | 3.0458043268232097e-06 | 2.8635381090256196e-06 | 5.98% | 6.37% | 1.06x | ✅ |
