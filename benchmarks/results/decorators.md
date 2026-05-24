#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.2300268954335424e-05 | 2.5642785777682487e-05 | -108.47% | -52.03% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.5145995439604657e-06 | 1.5245618015359931e-06 | -0.66% | -0.65% | 0.99x | ❌ |
| `replace_exceptions[unmapped-exception]` | 8.82956338498165e-06 | 1.5466582662655046e-05 | -75.17% | -42.91% | 0.57x | ❌ |
| `return_arg_type[float-pos0]` | 2.384874391691149e-06 | 2.2165472713890087e-06 | 7.06% | 7.59% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.365975897280614e-06 | 2.181098989837965e-06 | 7.81% | 8.48% | 1.08x | ✅ |
| `return_arg_type[int-pos1]` | 2.31652237611612e-06 | 2.0747353924587254e-06 | 10.44% | 11.65% | 1.12x | ✅ |
| `return_arg_type[str-pos0]` | 2.8836293621994786e-06 | 2.822088596123078e-06 | 2.13% | 2.18% | 1.02x | ✅ |
| `return_arg_type[str-pos1]` | 2.7896447781347595e-06 | 2.7578442675772566e-06 | 1.14% | 1.15% | 1.01x | ✅ |
