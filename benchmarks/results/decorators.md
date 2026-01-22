#### [faster_eth_utils.decorators](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/decorators.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_decorators_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `replace_exceptions[mapped-exception]` | 1.1297280548364732e-05 | 2.1803255984966342e-05 | -93.00% | -48.19% | 0.52x | ❌ |
| `replace_exceptions[no-exception]` | 1.4241222226982836e-06 | 1.3917751849063692e-06 | 2.27% | 2.32% | 1.02x | ✅ |
| `replace_exceptions[unmapped-exception]` | 8.230285680964442e-06 | 1.282639743274246e-05 | -55.84% | -35.83% | 0.64x | ❌ |
| `return_arg_type[float-pos0]` | 2.2153880271135747e-06 | 2.0464985389599172e-06 | 7.62% | 8.25% | 1.08x | ✅ |
| `return_arg_type[int-pos0]` | 2.1675520868367346e-06 | 2.027032502135556e-06 | 6.48% | 6.93% | 1.07x | ✅ |
| `return_arg_type[int-pos1]` | 2.1063059729773622e-06 | 1.9563372065046473e-06 | 7.12% | 7.67% | 1.08x | ✅ |
| `return_arg_type[str-pos0]` | 2.7532992686724157e-06 | 2.5716005736457313e-06 | 6.60% | 7.07% | 1.07x | ✅ |
| `return_arg_type[str-pos1]` | 2.758662223801805e-06 | 2.5757201248735357e-06 | 6.63% | 7.10% | 1.07x | ✅ |
