#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.892145607591579e-05 | 7.382094271062675e-05 | -7.11% | -6.64% | 0.93x | ❌ |
| `clamp[at-lower]` | 6.899041258506953e-05 | 7.20950046842974e-05 | -4.50% | -4.31% | 0.96x | ❌ |
| `clamp[at-upper]` | 6.956308650998861e-05 | 7.159834205617062e-05 | -2.93% | -2.84% | 0.97x | ❌ |
| `clamp[below-lower]` | 6.316465682129228e-05 | 6.268314760605251e-05 | 0.76% | 0.77% | 1.01x | ✅ |
| `clamp[within-bounds]` | 6.813056038571864e-05 | 7.038647648889526e-05 | -3.31% | -3.21% | 0.97x | ❌ |
