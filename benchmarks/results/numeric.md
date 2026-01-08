#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.576176179907844e-05 | 6.564739144087238e-05 | 13.35% | 15.41% | 1.15x | ✅ |
| `clamp[at-lower]` | 7.48839168502857e-05 | 6.456592371622386e-05 | 13.78% | 15.98% | 1.16x | ✅ |
| `clamp[at-upper]` | 7.266191010403188e-05 | 6.549886885050017e-05 | 9.86% | 10.94% | 1.11x | ✅ |
| `clamp[below-lower]` | 6.959352851317239e-05 | 5.748326609151826e-05 | 17.40% | 21.07% | 1.21x | ✅ |
| `clamp[within-bounds]` | 7.520273726501767e-05 | 6.683227609764442e-05 | 11.13% | 12.52% | 1.13x | ✅ |
