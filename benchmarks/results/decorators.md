#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.178217848431718e-05 | 2.4278213560676532e-05 | -106.06% | -51.47% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.5283324853775137e-06 | 1.4709028247884446e-06 | 3.76% | 3.90% | 1.04x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.588012014795032e-06 | 1.4466464831772366e-05 | -68.45% | -40.64% | 0.59x | ❌ |
| `return_arg_type[float-pos0]` | 2.4095864853002204e-06 | 2.156672324192707e-06 | 10.50% | 11.73% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.352332163410952e-06 | 2.1169183487405906e-06 | 10.01% | 11.12% | 1.11x | ✅ |
| `return_arg_type[int-pos1]` | 2.2947158895425883e-06 | 2.0344204898176808e-06 | 11.34% | 12.79% | 1.13x | ✅ |
| `return_arg_type[str-pos0]` | 2.94205583907022e-06 | 2.792972304702656e-06 | 5.07% | 5.34% | 1.05x | ✅ |
| `return_arg_type[str-pos1]` | 2.851897390540316e-06 | 2.7164161676958857e-06 | 4.75% | 4.99% | 1.05x | ✅ |
