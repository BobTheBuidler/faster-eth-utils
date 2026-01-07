#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1967205945121487e-05 | 2.4612725901319374e-05 | -105.67% | -51.38% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6571763118786776e-06 | 1.503306700860205e-06 | 9.29% | 10.24% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.387485801584113e-06 | 1.4674120148311509e-05 | -74.95% | -42.84% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.487951051321252e-06 | 2.400923205179092e-06 | 3.50% | 3.62% | 1.04x | ✅ |
| `return_arg_type[int-pos0]` | 2.405475676682652e-06 | 2.276640776698652e-06 | 5.36% | 5.66% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.322659788340247e-06 | 2.1867727356042532e-06 | 5.85% | 6.21% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 3.158014298721753e-06 | 2.772111698617576e-06 | 12.22% | 13.92% | 1.14x | ✅ |
| `return_arg_type[str-pos1]` | 3.057562699799428e-06 | 2.7744706982906006e-06 | 9.26% | 10.20% | 1.10x | ✅ |
