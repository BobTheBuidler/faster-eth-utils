#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.463967023475274e-05 | 6.718695084220525e-05 | 9.98% | 11.09% | 1.11x | ✅ |
| `clamp[at-lower]` | 7.253742192321524e-05 | 6.627939598050332e-05 | 8.63% | 9.44% | 1.09x | ✅ |
| `clamp[at-upper]` | 7.162764363139156e-05 | 6.635449841263454e-05 | 7.36% | 7.95% | 1.08x | ✅ |
| `clamp[below-lower]` | 6.822783189218148e-05 | 5.920851954954373e-05 | 13.22% | 15.23% | 1.15x | ✅ |
| `clamp[within-bounds]` | 7.172384689020903e-05 | 6.767682527768521e-05 | 5.64% | 5.98% | 1.06x | ✅ |
