#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2466968753636357e-05 | 2.4867442582948505e-05 | -99.47% | -49.87% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.567199586418999e-06 | 1.495155702547405e-06 | 4.60% | 4.82% | 1.05x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.739137737003808e-06 | 1.4956418169293975e-05 | -71.14% | -41.57% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.472407761184624e-06 | 2.2365353414198593e-06 | 9.54% | 10.55% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.5044842570643727e-06 | 2.2582677267651495e-06 | 9.83% | 10.90% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.4594053428120405e-06 | 2.206938248309191e-06 | 10.27% | 11.44% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 3.0988900956480554e-06 | 2.895582500552903e-06 | 6.56% | 7.02% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 3.1595761981116636e-06 | 2.794946263133375e-06 | 11.54% | 13.05% | 1.13x | ✅ |
