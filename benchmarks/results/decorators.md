#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.191183084370568e-05 | 2.4154939781653095e-05 | -102.78% | -50.69% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6132665297008608e-06 | 1.4858262815478742e-06 | 7.90% | 8.58% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.348779323336113e-06 | 1.4591173163694373e-05 | -74.77% | -42.78% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.5214839289197847e-06 | 2.328374065309374e-06 | 7.66% | 8.29% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.407491632021292e-06 | 2.2952227828070677e-06 | 4.66% | 4.89% | 1.05x | ✅ |
| `return_arg_type[int-pos1]` | 2.3402227803480616e-06 | 2.2453482801555717e-06 | 4.05% | 4.23% | 1.04x | ✅ |
| `return_arg_type[str-pos0]` | 3.137561780490276e-06 | 2.893069825927041e-06 | 7.79% | 8.45% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 3.047520769439271e-06 | 2.900737929563191e-06 | 4.82% | 5.06% | 1.05x | ✅ |
