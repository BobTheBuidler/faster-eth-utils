#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1817760584559608e-05 | 2.4021763312277967e-05 | -103.27% | -50.80% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5051678340002069e-06 | 1.485175032491915e-06 | 1.33% | 1.35% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.485218740170478e-06 | 1.4358286793147597e-05 | -69.22% | -40.90% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.391718040443626e-06 | 2.1071515457319307e-06 | 11.90% | 13.50% | 1.14x | ✅ |
| `return_arg_type[int-pos0]` | 2.3207358861300933e-06 | 2.1187850128961344e-06 | 8.70% | 9.53% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.330822610077599e-06 | 1.994483452551893e-06 | 14.43% | 16.86% | 1.17x | ✅ |
| `return_arg_type[str-pos0]` | 2.968848663054834e-06 | 2.8538528734386033e-06 | 3.87% | 4.03% | 1.04x | ✅ |
| `return_arg_type[str-pos1]` | 2.9189122346666444e-06 | 2.83447126446279e-06 | 2.89% | 2.98% | 1.03x | ✅ |
