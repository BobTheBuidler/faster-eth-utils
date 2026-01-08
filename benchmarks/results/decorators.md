#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1891018180253293e-05 | 2.4339083153532178e-05 | -104.68% | -51.14% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6554181653291712e-06 | 1.5115776041549561e-06 | 8.69% | 9.52% | 1.10x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.415932550022834e-06 | 1.4534289765394486e-05 | -72.70% | -42.10% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4989243053957163e-06 | 2.3719949438364737e-06 | 5.08% | 5.35% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.4238632240469064e-06 | 2.3443288695555767e-06 | 3.28% | 3.39% | 1.03x | ✅ |
| `return_arg_type[int-pos1]` | 2.3826665206288396e-06 | 2.196832353403691e-06 | 7.80% | 8.46% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 3.1195940222881063e-06 | 2.8585438974446492e-06 | 8.37% | 9.13% | 1.09x | ✅ |
| `return_arg_type[str-pos1]` | 3.078791249093126e-06 | 2.8244234331704978e-06 | 8.26% | 9.01% | 1.09x | ✅ |
