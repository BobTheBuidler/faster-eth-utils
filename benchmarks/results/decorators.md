#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1791777552263591e-05 | 2.4361849439238613e-05 | -106.60% | -51.60% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5960036710210006e-06 | 1.4855393296743448e-06 | 6.92% | 7.44% | 1.07x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.289610737290463e-06 | 1.4541127720033312e-05 | -75.41% | -42.99% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.444024576407909e-06 | 2.279962968562261e-06 | 6.71% | 7.20% | 1.07x | ✅ |
| `return_arg_type[int-pos0]` | 2.433276121113884e-06 | 2.2515099771288443e-06 | 7.47% | 8.07% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.3897948987236697e-06 | 2.169265263753026e-06 | 9.23% | 10.17% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 3.128459907426572e-06 | 2.914059783095476e-06 | 6.85% | 7.36% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 3.070918731680778e-06 | 2.870115074226419e-06 | 6.54% | 7.00% | 1.07x | ✅ |
