#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2068971009593326e-05 | 2.4548614705931027e-05 | -103.40% | -50.84% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6769598929135483e-06 | 1.5161074036312092e-06 | 9.59% | 10.61% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.425512985590011e-06 | 1.4644729730270607e-05 | -73.81% | -42.47% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.562745560859932e-06 | 2.2981830931196526e-06 | 10.32% | 11.51% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.472987117582383e-06 | 2.286951542344602e-06 | 7.52% | 8.13% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.352244641729323e-06 | 2.2234797669276883e-06 | 5.47% | 5.79% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 3.1965289641197093e-06 | 2.953594505854211e-06 | 7.60% | 8.23% | 1.08x | ✅ |
| `return_arg_type[str-pos1]` | 3.1006787406258233e-06 | 2.855894720962111e-06 | 7.89% | 8.57% | 1.09x | ✅ |
