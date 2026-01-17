#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.199732449154335e-05 | 2.446674808815965e-05 | -103.94% | -50.96% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6230943422153183e-06 | 1.4616549197775457e-06 | 9.95% | 11.04% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.379204872163051e-06 | 1.4428143134280119e-05 | -72.19% | -41.92% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.5141404503826405e-06 | 2.251616465051254e-06 | 10.44% | 11.66% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.416063274056129e-06 | 2.2157583111916917e-06 | 8.29% | 9.04% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.3848389280185e-06 | 2.15026022704236e-06 | 9.84% | 10.91% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 3.1702057404629427e-06 | 2.835300256557697e-06 | 10.56% | 11.81% | 1.12x | ✅ |
| `return_arg_type[str-pos1]` | 3.087760711273904e-06 | 2.9171960769681815e-06 | 5.52% | 5.85% | 1.06x | ✅ |
