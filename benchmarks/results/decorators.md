#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.284951797689539e-05 | 2.5958092238666298e-05 | -102.02% | -50.50% | 0.50x | ❌ |
| `replace_exceptions[no-exception]` | 1.5294786549680612e-06 | 1.5208185871738587e-06 | 0.57% | 0.57% | 1.01x | ✅ |
| `replace_exceptions[unmapped-exception]` | 9.297831883729795e-06 | 1.5287097433726338e-05 | -64.42% | -39.18% | 0.61x | ❌ |
| `return_arg_type[float-pos0]` | 2.5021466954894396e-06 | 2.1630364390984583e-06 | 13.55% | 15.68% | 1.16x | ✅ |
| `return_arg_type[int-pos0]` | 2.3567862531613755e-06 | 2.19661449893149e-06 | 6.80% | 7.29% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.3389579117880387e-06 | 2.127448152032539e-06 | 9.04% | 9.94% | 1.10x | ✅ |
| `return_arg_type[str-pos0]` | 2.896595707999184e-06 | 2.713758174162513e-06 | 6.31% | 6.74% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.9162507822794204e-06 | 2.6968289476715085e-06 | 7.52% | 8.14% | 1.08x | ✅ |
