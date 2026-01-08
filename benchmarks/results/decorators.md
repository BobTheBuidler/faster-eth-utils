#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.210054096453666e-05 | 2.4012515819348287e-05 | -98.44% | -49.61% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.622634511203799e-06 | 1.4939038327526599e-06 | 7.93% | 8.62% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.37683089339587e-06 | 1.4587494234054496e-05 | -74.14% | -42.58% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.4486752511698306e-06 | 2.3605471156475203e-06 | 3.60% | 3.73% | 1.04x | ✅ |
| `return_arg_type[int-pos0]` | 2.405340288468747e-06 | 2.2645026254091514e-06 | 5.86% | 6.22% | 1.06x | ✅ |
| `return_arg_type[int-pos1]` | 2.3164844766301986e-06 | 2.205056910988333e-06 | 4.81% | 5.05% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.14908251208685e-06 | 2.7844632134502883e-06 | 11.58% | 13.09% | 1.13x | ✅ |
| `return_arg_type[str-pos1]` | 3.0867268701235286e-06 | 2.77641975615824e-06 | 10.05% | 11.18% | 1.11x | ✅ |
