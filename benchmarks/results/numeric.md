#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.151917634346708e-05 | 7.572713217093618e-05 | -5.88% | -5.56% | 0.94x | ❌ |
| `clamp[at-lower]` | 7.307276935234207e-05 | 7.554008664254345e-05 | -3.38% | -3.27% | 0.97x | ❌ |
| `clamp[at-upper]` | 7.130500126282407e-05 | 7.548146585346502e-05 | -5.86% | -5.53% | 0.94x | ❌ |
| `clamp[below-lower]` | 6.554622275557116e-05 | 6.474116267306963e-05 | 1.23% | 1.24% | 1.01x | ✅ |
| `clamp[within-bounds]` | 7.268818166328098e-05 | 7.689539466511556e-05 | -5.79% | -5.47% | 0.95x | ❌ |
