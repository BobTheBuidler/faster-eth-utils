#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 6.889356559972724e-05 | 7.106297882279855e-05 | -3.15% | -3.05% | 0.97x | ❌ |
| `clamp[at-lower]` | 6.724402331959515e-05 | 7.174445928883314e-05 | -6.69% | -6.27% | 0.94x | ❌ |
| `clamp[at-upper]` | 6.736554047349089e-05 | 7.181051038356324e-05 | -6.60% | -6.19% | 0.94x | ❌ |
| `clamp[below-lower]` | 6.34425461801538e-05 | 6.226808054701514e-05 | 1.85% | 1.89% | 1.02x | ✅ |
| `clamp[within-bounds]` | 6.816795016999581e-05 | 7.460326089995205e-05 | -9.44% | -8.63% | 0.91x | ❌ |
