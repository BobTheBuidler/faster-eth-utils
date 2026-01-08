#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1976245180038475e-05 | 2.4269472967804964e-05 | -102.65% | -50.65% | 0.49x | ❌ |
| `replace_exceptions[no-exception]` | 1.6847161240240434e-06 | 1.5213924436716412e-06 | 9.69% | 10.74% | 1.11x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.418322260862352e-06 | 1.4592942641439979e-05 | -73.35% | -42.31% | 0.58x | ❌ |
| `return_arg_type[float-pos0]` | 2.531116815919507e-06 | 2.3785146719453092e-06 | 6.03% | 6.42% | 1.06x | ✅ |
| `return_arg_type[int-pos0]` | 2.415053908274947e-06 | 2.31869322952821e-06 | 3.99% | 4.16% | 1.04x | ✅ |
| `return_arg_type[int-pos1]` | 2.3716359467170964e-06 | 2.268251926205293e-06 | 4.36% | 4.56% | 1.05x | ✅ |
| `return_arg_type[str-pos0]` | 3.2615268324043337e-06 | 2.874295465157236e-06 | 11.87% | 13.47% | 1.13x | ✅ |
| `return_arg_type[str-pos1]` | 3.1164713139069908e-06 | 2.8044861520891127e-06 | 10.01% | 11.12% | 1.11x | ✅ |
