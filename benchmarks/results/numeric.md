#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.883812620440478e-05 | 6.686170511859216e-05 | 2.87% | 2.96% | 1.03x | ✅ |
| `clamp[at-lower]` | 6.431451086675811e-05 | 6.941065765267916e-05 | -7.92% | -7.34% | 0.93x | ❌ |
| `clamp[at-upper]` | 6.725277596458547e-05 | 6.820521187860215e-05 | -1.42% | -1.40% | 0.99x | ❌ |
| `clamp[below-lower]` | 6.224557534689287e-05 | 5.975684830581739e-05 | 4.00% | 4.16% | 1.04x | ✅ |
| `clamp[within-bounds]` | 6.398501260795533e-05 | 6.828769948974876e-05 | -6.72% | -6.30% | 0.94x | ❌ |
