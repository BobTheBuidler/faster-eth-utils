#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1728346669692353e-05 | 2.3809194747844057e-05 | -103.01% | -50.74% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5591976681375925e-06 | 1.4056398015156252e-06 | 9.85% | 10.92% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.477992339917258e-06 | 1.4308378569372989e-05 | -68.77% | -40.75% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.3345573462096814e-06 | 2.1501340920976375e-06 | 7.90% | 8.58% | 1.09x | ✅ |
| `return_arg_type[int-pos0]` | 2.2991901425402253e-06 | 2.0712335437656216e-06 | 9.91% | 11.01% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.284672388322959e-06 | 1.9710560044130964e-06 | 13.73% | 15.91% | 1.16x | ✅ |
| `return_arg_type[str-pos0]` | 2.8847170644043716e-06 | 2.7814874084809157e-06 | 3.58% | 3.71% | 1.04x | ✅ |
| `return_arg_type[str-pos1]` | 2.9261715185586227e-06 | 2.775409696802248e-06 | 5.15% | 5.43% | 1.05x | ✅ |
