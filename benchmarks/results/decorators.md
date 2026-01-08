#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1855644242758666e-05 | 2.4541591652863588e-05 | -107.00% | -51.69% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.610157233678622e-06 | 1.4812273377117953e-06 | 8.01% | 8.70% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.403333570193166e-06 | 1.4899036817524582e-05 | -77.30% | -43.60% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.502301435647226e-06 | 2.376179275990051e-06 | 5.04% | 5.31% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.397310591783239e-06 | 2.262259281361038e-06 | 5.63% | 5.97% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3496535657992905e-06 | 2.1671722578445514e-06 | 7.77% | 8.42% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.1293475218406977e-06 | 2.881262497550092e-06 | 7.93% | 8.61% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.0689703755155347e-06 | 2.7861328327944957e-06 | 9.22% | 10.15% | 1.10x | ✅ |
