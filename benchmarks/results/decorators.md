#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2063155359306211e-05 | 2.5305165727347958e-05 | -109.77% | -52.33% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5269923157294905e-06 | 1.4611596752517245e-06 | 4.31% | 4.51% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.54608245384092e-06 | 1.5113698301991634e-05 | -76.85% | -43.45% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.324832471704395e-06 | 2.259997314352775e-06 | 2.79% | 2.87% | 1.03x | ✅ |
| `return_arg_type[int-pos0]` | 2.303019619884582e-06 | 2.206175788337163e-06 | 4.21% | 4.39% | 1.04x | ✅ |
| `return_arg_type[int-pos1]` | 2.2538406242696846e-06 | 2.117754916949748e-06 | 6.04% | 6.43% | 1.06x | ✅ |
| `return_arg_type[str-pos0]` | 2.844246275683996e-06 | 2.8311310758447778e-06 | 0.46% | 0.46% | 1.00x | ✅ |
| `return_arg_type[str-pos1]` | 2.8447321708664635e-06 | 2.759780271067712e-06 | 2.99% | 3.08% | 1.03x | ✅ |
