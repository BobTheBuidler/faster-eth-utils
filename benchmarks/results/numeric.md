#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 5.9078701230773256e-05 | 6.148128400485413e-05 | -4.07% | -3.91% | 0.96x | ❌ |
| `clamp[at-lower]` | 5.913479579707699e-05 | 6.158568485542704e-05 | -4.14% | -3.98% | 0.96x | ❌ |
| `clamp[at-upper]` | 5.899523685692579e-05 | 6.173692990282588e-05 | -4.65% | -4.44% | 0.96x | ❌ |
| `clamp[below-lower]` | 5.270909057210298e-05 | 5.435399010660316e-05 | -3.12% | -3.03% | 0.97x | ❌ |
| `clamp[within-bounds]` | 5.912393052909948e-05 | 6.208912296900143e-05 | -5.02% | -4.78% | 0.95x | ❌ |
