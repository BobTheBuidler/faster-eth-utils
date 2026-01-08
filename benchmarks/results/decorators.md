#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1840174869495457e-05 | 2.4294667556249467e-05 | -105.19% | -51.26% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6204693265905847e-06 | 1.466654452957855e-06 | 9.49% | 10.49% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.363390250251464e-06 | 1.4502659284674923e-05 | -73.41% | -42.33% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4608404762624143e-06 | 2.39560658415739e-06 | 2.65% | 2.72% | 1.03x | ✅ |
| `return_arg_type[int-pos0]` | 2.390200182056159e-06 | 2.2602376568214705e-06 | 5.44% | 5.75% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3714724901473147e-06 | 2.1713861439277483e-06 | 8.44% | 9.21% | 1.09x | ✅ |
| `return_arg_type[str-pos0]` | 3.0386936384294735e-06 | 2.814980641522338e-06 | 7.36% | 7.95% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 3.0652541800121875e-06 | 2.7314477293223067e-06 | 10.89% | 12.22% | 1.12x | ✅ |
