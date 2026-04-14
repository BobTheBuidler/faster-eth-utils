#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1691799916892685e-05 | 2.492240482373657e-05 | -113.16% | -53.09% | 0.47x | ❌ |
| `replace_exceptions[no-exception]` | 1.509652502792179e-06 | 1.5058517819233304e-06 | 0.25% | 0.25% | 1.00x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.25934001324775e-06 | 1.4804734232064453e-05 | -79.25% | -44.21% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.4454623013893294e-06 | 2.184361007795332e-06 | 10.68% | 11.95% | 1.12x | ✅ |
| `return_arg_type[int-pos0]` | 2.3363878363593013e-06 | 2.1330558690382896e-06 | 8.70% | 9.53% | 1.10x | ✅ |
| `return_arg_type[int-pos1]` | 2.2725559842753514e-06 | 2.0414089416606575e-06 | 10.17% | 11.32% | 1.11x | ✅ |
| `return_arg_type[str-pos0]` | 2.9175228077797585e-06 | 2.602286939180672e-06 | 10.80% | 12.11% | 1.12x | ✅ |
| `return_arg_type[str-pos1]` | 2.9277640036924834e-06 | 2.5854602795862244e-06 | 11.69% | 13.24% | 1.13x | ✅ |
