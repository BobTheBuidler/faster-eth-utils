#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.181891574743165e-05 | 2.5053248442345444e-05 | -111.98% | -52.82% | 0.47x | ❌ |
| `replace_exceptions[no-exception]` | 1.5891548814283394e-06 | 1.4583160021359912e-06 | 8.23% | 8.97% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.335374590263173e-06 | 1.4898135891802746e-05 | -78.73% | -44.05% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.5702699753186845e-06 | 2.3298516785789743e-06 | 9.35% | 10.32% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.5304391019847137e-06 | 2.330797684614299e-06 | 7.89% | 8.57% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.3939280938031374e-06 | 2.2465896100452142e-06 | 6.15% | 6.56% | 1.07x | ✅ |
| `return_arg_type[str-pos0]` | 3.2213763487065165e-06 | 2.9256269411052364e-06 | 9.18% | 10.11% | 1.10x | ✅ |
| `return_arg_type[str-pos1]` | 3.14841789152416e-06 | 2.8482838678709162e-06 | 9.53% | 10.54% | 1.11x | ✅ |
