#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2170424987444218e-05 | 2.2519518977331923e-05 | -85.03% | -45.96% | 0.54x | ❌ |
| `replace_exceptions[no-exception]` | 1.5422322169477638e-06 | 1.6208060103084362e-06 | -5.09% | -4.85% | 0.95x | ❌ |
| `replace_exceptions[unmapped-exception]` | 8.745872065599738e-06 | 1.3547072310736427e-05 | -54.90% | -35.44% | 0.65x | ❌ |
| `return_arg_type[float-pos0]` | 2.5746170159261605e-06 | 2.3447460995822892e-06 | 8.93% | 9.80% | 1.10x | ✅ |
| `return_arg_type[int-pos0]` | 2.969575466283762e-06 | 2.7170930063920276e-06 | 8.50% | 9.29% | 1.09x | ✅ |
| `return_arg_type[int-pos1]` | 2.8865013934618677e-06 | 2.6323126327439535e-06 | 8.81% | 9.66% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.923671486449095e-06 | 3.2193166040536556e-06 | -10.11% | -9.18% | 0.91x | ❌ |
| `return_arg_type[str-pos1]` | 2.845384240237042e-06 | 3.15351777183201e-06 | -10.83% | -9.77% | 0.90x | ❌ |
