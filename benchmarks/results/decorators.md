#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1641560824222685e-05 | 2.430540080213052e-05 | -108.78% | -52.10% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5471587458356037e-06 | 1.4202920601622892e-06 | 8.20% | 8.93% | 1.09x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.627000081881935e-06 | 1.481371433500822e-05 | -71.71% | -41.76% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.4210350546060628e-06 | 2.1790334524389156e-06 | 10.00% | 11.11% | 1.11x | ✅ |
| `return_arg_type[int-pos0]` | 2.3183796813972055e-06 | 2.0897507127523065e-06 | 9.86% | 10.94% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.295396536750217e-06 | 1.9716199215159846e-06 | 14.11% | 16.42% | 1.16x | ✅ |
| `return_arg_type[str-pos0]` | 2.7898722176454464e-06 | 2.6448157994690944e-06 | 5.20% | 5.48% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 2.804490405700336e-06 | 2.6418792141706825e-06 | 5.80% | 6.16% | 1.06x | ✅ |
