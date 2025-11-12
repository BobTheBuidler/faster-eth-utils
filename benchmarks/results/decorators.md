#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1595975930767604e-05 | 2.4719324389425716e-05 | -113.17% | -53.09% | 0.47x | ❌ |
| `replace_exceptions[no-exception]` | 1.4747723175060642e-06 | 1.419812687895998e-06 | 3.73% | 3.87% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.402143160881528e-06 | 1.4798580183943285e-05 | -76.13% | -43.22% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.3621796862193525e-06 | 2.125278451727303e-06 | 10.03% | 11.15% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.3653546110437586e-06 | 2.1223536682056273e-06 | 10.27% | 11.45% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.330700686157163e-06 | 2.028972328336616e-06 | 12.95% | 14.87% | 1.15x | ✅ |
| `return_arg_type[str-pos0]` | 3.002983344765647e-06 | 2.7346653425080822e-06 | 8.94% | 9.81% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 2.958336177608937e-06 | 2.758004966082598e-06 | 6.77% | 7.26% | 1.07x | ✅ |
