#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2639778164174476e-05 | 3.0300140021450866e-05 | -139.72% | -58.28% | 0.42x | ❌ |
| `replace_exceptions[no-exception]` | 1.5463115486143071e-06 | 1.4385959582482033e-06 | 6.97% | 7.49% | 1.07x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.985240877662122e-06 | 1.628255841701838e-05 | -81.21% | -44.82% | 0.55x | ❌ |
| `return_arg_type[float-pos0]` | 2.5122390241141923e-06 | 2.3648016596396195e-06 | 5.87% | 6.23% | 1.06x | ✅ |
| `return_arg_type[int-pos0]` | 2.4207860128729795e-06 | 2.2391976839375586e-06 | 7.50% | 8.11% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.3627749606776707e-06 | 2.1405818156727658e-06 | 9.40% | 10.38% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.9352075032532456e-06 | 2.998655675497748e-06 | -2.16% | -2.12% | 0.98x | ❌ |
| `return_arg_type[str-pos1]` | 2.928611670492265e-06 | 3.015784130550751e-06 | -2.98% | -2.89% | 0.97x | ❌ |
