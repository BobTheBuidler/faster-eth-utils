#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1864869621795976e-05 | 2.423171003987712e-05 | -104.23% | -51.04% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6966368038458496e-06 | 1.50809058168853e-06 | 11.11% | 12.50% | 1.13x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.342838774748514e-06 | 1.4540422520212765e-05 | -74.29% | -42.62% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.5126798250010178e-06 | 2.384834771313332e-06 | 5.09% | 5.36% | 1.05x | ✅ |
| `return_arg_type[int-pos0]` | 2.4557997236297375e-06 | 2.2481246834970664e-06 | 8.46% | 9.24% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.3947195194755754e-06 | 2.180507972770523e-06 | 8.95% | 9.82% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 3.1326153752097748e-06 | 2.767372458579522e-06 | 11.66% | 13.20% | 1.13x | ✅ |
| `return_arg_type[str-pos1]` | 3.127898153035937e-06 | 2.7728549521041916e-06 | 11.35% | 12.80% | 1.13x | ✅ |
