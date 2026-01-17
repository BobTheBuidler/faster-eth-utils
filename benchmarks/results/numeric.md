#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.288848266192479e-05 | 6.594680962743383e-05 | 9.52% | 10.53% | 1.11x | ✅ |
| `clamp[at-lower]` | 7.444501147717202e-05 | 6.401527443833027e-05 | 14.01% | 16.29% | 1.16x | ✅ |
| `clamp[at-upper]` | 7.241576615049025e-05 | 6.601970943421605e-05 | 8.83% | 9.69% | 1.10x | ✅ |
| `clamp[below-lower]` | 6.598472915730766e-05 | 5.901709832649461e-05 | 10.56% | 11.81% | 1.12x | ✅ |
| `clamp[within-bounds]` | 7.151527148591445e-05 | 6.616658350242283e-05 | 7.48% | 8.08% | 1.08x | ✅ |
