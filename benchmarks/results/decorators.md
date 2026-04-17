#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.250075538386618e-05 | 2.5874764296135935e-05 | -106.99% | -51.69% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6311980878782936e-06 | 1.5663365129422568e-06 | 3.98% | 4.14% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.87810231010119e-06 | 1.54428908940452e-05 | -73.94% | -42.51% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.488686462051259e-06 | 2.436431701065267e-06 | 2.10% | 2.14% | 1.02x | ✅ |
| `return_arg_type[int-pos0]` | 2.4378891469984174e-06 | 2.3761192725546575e-06 | 2.53% | 2.60% | 1.03x | ✅ |
| `return_arg_type[int-pos1]` | 2.3941117170311692e-06 | 2.299259814302931e-06 | 3.96% | 4.13% | 1.04x | ✅ |
| `return_arg_type[str-pos0]` | 3.0026213531239325e-06 | 2.9312363340817313e-06 | 2.38% | 2.44% | 1.02x | ✅ |
| `return_arg_type[str-pos1]` | 3.0205918739471717e-06 | 2.93253466251907e-06 | 2.92% | 3.00% | 1.03x | ✅ |
