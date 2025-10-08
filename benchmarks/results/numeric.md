#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 8.527386796742427e-07 | 8.699013283382799e-07 | -2.01% | -1.97% | 0.98x | ❌ |
| `clamp[at-lower]` | 8.316378878501071e-07 | 8.642744788012553e-07 | -3.92% | -3.78% | 0.96x | ❌ |
| `clamp[at-upper]` | 8.283836837191971e-07 | 8.581072907705225e-07 | -3.59% | -3.46% | 0.97x | ❌ |
| `clamp[below-lower]` | 8.216412421863271e-07 | 9.022266224015615e-07 | -9.81% | -8.93% | 0.91x | ❌ |
| `clamp[within-bounds]` | 8.294682157315061e-07 | 8.686509822204761e-07 | -4.72% | -4.51% | 0.95x | ❌ |
