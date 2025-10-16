#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.217219032769998e-05 | 6.917238639627497e-05 | 4.16% | 4.34% | 1.04x | ✅ |
| `clamp[at-lower]` | 7.02887237401581e-05 | 6.940520533331508e-05 | 1.26% | 1.27% | 1.01x | ✅ |
| `clamp[at-upper]` | 7.100280168882993e-05 | 7.051839037478745e-05 | 0.68% | 0.69% | 1.01x | ✅ |
| `clamp[below-lower]` | 6.669303759756453e-05 | 6.223912453260779e-05 | 6.68% | 7.16% | 1.07x | ✅ |
| `clamp[within-bounds]` | 7.136288107255182e-05 | 7.190126619903969e-05 | -0.75% | -0.75% | 0.99x | ❌ |
