#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.277809600460531e-05 | 2.5943555900790083e-05 | -103.03% | -50.75% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.525678988738401e-06 | 1.4833740369802781e-06 | 2.77% | 2.85% | 1.03x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.93224981841488e-06 | 1.547263994488171e-05 | -73.22% | -42.27% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4513438067466934e-06 | 2.2778972700176694e-06 | 7.08% | 7.61% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.478788130223005e-06 | 2.386134298728818e-06 | 3.74% | 3.88% | 1.04x | ✅ |
| `return_arg_type[int-pos1]` | 2.399487031195358e-06 | 2.3180278355939246e-06 | 3.39% | 3.51% | 1.04x | ✅ |
| `return_arg_type[str-pos0]` | 3.062457080724326e-06 | 2.9106159846360596e-06 | 4.96% | 5.22% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 3.072554471733107e-06 | 2.92080902434611e-06 | 4.94% | 5.20% | 1.05x | ✅ |
