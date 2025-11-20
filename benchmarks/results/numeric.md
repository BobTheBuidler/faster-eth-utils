#### [faster_eth_utils.numeric](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/numeric.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_numeric_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `clamp[above-upper]` | 7.264611883201108e-05 | 7.053556685733358e-05 | 2.91% | 2.99% | 1.03x | ✅ |
| `clamp[at-lower]` | 7.327247023167308e-05 | 7.0478694036937e-05 | 3.81% | 3.96% | 1.04x | ✅ |
| `clamp[at-upper]` | 7.30732381024116e-05 | 7.07670199926184e-05 | 3.16% | 3.26% | 1.03x | ✅ |
| `clamp[below-lower]` | 6.623831767379172e-05 | 6.271738913991516e-05 | 5.32% | 5.61% | 1.06x | ✅ |
| `clamp[within-bounds]` | 7.110174038090029e-05 | 7.153663283666056e-05 | -0.61% | -0.61% | 0.99x | ❌ |
