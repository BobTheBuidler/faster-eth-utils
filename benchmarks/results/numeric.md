#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.535127910714633e-05 | 6.514017671546498e-05 | 13.55% | 15.68% | 1.16x | ✅ |
| `clamp[at-lower]` | 7.212904532473814e-05 | 6.805024581560003e-05 | 5.65% | 5.99% | 1.06x | ✅ |
| `clamp[at-upper]` | 7.261457120820479e-05 | 6.584083758762921e-05 | 9.33% | 10.29% | 1.10x | ✅ |
| `clamp[below-lower]` | 6.897120268875295e-05 | 5.830316086903174e-05 | 15.47% | 18.30% | 1.18x | ✅ |
| `clamp[within-bounds]` | 7.254605100871824e-05 | 6.617223560463933e-05 | 8.79% | 9.63% | 1.10x | ✅ |
