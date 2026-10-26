#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2251151681784476e-05 | 2.5272810697837377e-05 | -106.29% | -51.52% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5345871836123617e-06 | 1.443291141331855e-06 | 5.95% | 6.33% | 1.06x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.841386342242151e-06 | 1.5341980561244883e-05 | -73.52% | -42.37% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.398622418704668e-06 | 2.333975540956144e-06 | 2.70% | 2.77% | 1.03x | ✅ |
| `return_arg_type[int-pos0]` | 2.29742849625304e-06 | 2.2309830201599653e-06 | 2.89% | 2.98% | 1.03x | ✅ |
| `return_arg_type[int-pos1]` | 2.205338333284508e-06 | 2.1459538998268397e-06 | 2.69% | 2.77% | 1.03x | ✅ |
| `return_arg_type[str-pos0]` | 3.0033776968198033e-06 | 2.9078707913821874e-06 | 3.18% | 3.28% | 1.03x | ✅ |
| `return_arg_type[str-pos1]` | 2.8933273169986238e-06 | 2.843529896165571e-06 | 1.72% | 1.75% | 1.02x | ✅ |
