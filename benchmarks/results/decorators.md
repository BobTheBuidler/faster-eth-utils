#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1322910259181103e-05 | 2.3817187194597418e-05 | -110.35% | -52.46% | 0.48x | ❌ |
| `replace_exceptions[no-exception]` | 1.6083109250364746e-06 | 1.49330759605129e-06 | 7.15% | 7.70% | 1.08x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.16553231802742e-06 | 1.446825634916652e-05 | -77.19% | -43.56% | 0.56x | ❌ |
| `return_arg_type[float-pos0]` | 2.4548494008773866e-06 | 2.1172725627893164e-06 | 13.75% | 15.94% | 1.16x | ✅ |
| `return_arg_type[int-pos0]` | 2.372413673925614e-06 | 2.052106415878217e-06 | 13.50% | 15.61% | 1.16x | ✅ |
| `return_arg_type[int-pos1]` | 2.3256153483607073e-06 | 1.9885084836474733e-06 | 14.50% | 16.95% | 1.17x | ✅ |
| `return_arg_type[str-pos0]` | 2.8760028761744777e-06 | 2.591561565996633e-06 | 9.89% | 10.98% | 1.11x | ✅ |
| `return_arg_type[str-pos1]` | 2.846380693533807e-06 | 2.5829389021031506e-06 | 9.26% | 10.20% | 1.10x | ✅ |
