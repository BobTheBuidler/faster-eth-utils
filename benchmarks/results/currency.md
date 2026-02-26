#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.429288642902474e-05 | 2.3643663837503295e-05 | 2.67% | 2.75% | 1.03x | ✅ |
| `from_wei[1-gwei]` | 2.3854634357107024e-05 | 2.3346656210546855e-05 | 2.13% | 2.18% | 1.02x | ✅ |
| `from_wei[max]` | 2.5982140442759652e-05 | 2.5209514442013852e-05 | 2.97% | 3.06% | 1.03x | ✅ |
| `from_wei[zero]` | 2.6247369406997604e-06 | 2.150582405753978e-06 | 18.06% | 22.05% | 1.22x | ✅ |
| `from_wei_decimals[100M-8dec]` | 2.851065050429063e-05 | 2.8290890018226353e-05 | 0.77% | 0.78% | 1.01x | ✅ |
| `from_wei_decimals[max]` | 3.0264464417832167e-05 | 3.0247070559254986e-05 | 0.06% | 0.06% | 1.00x | ✅ |
| `from_wei_decimals[zero]` | 7.3381669375287604e-06 | 7.09119251654393e-06 | 3.37% | 3.48% | 1.03x | ✅ |
| `to_wei[1-ether]` | 3.2604976688332954e-05 | 2.841957137929093e-05 | 12.84% | 14.73% | 1.15x | ✅ |
| `to_wei[1.5-ether]` | 4.009590465462411e-05 | 3.623281396932456e-05 | 9.63% | 10.66% | 1.11x | ✅ |
| `to_wei[2str-ether]` | 3.241458700608495e-05 | 2.926914937965872e-05 | 9.70% | 10.75% | 1.11x | ✅ |
| `to_wei[max]` | 3.844753250219497e-05 | 3.4312032109126006e-05 | 10.76% | 12.05% | 1.12x | ✅ |
| `to_wei[zero]` | 9.20681657385353e-06 | 5.703118733593384e-06 | 38.06% | 61.43% | 1.61x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.640105400285645e-05 | 3.2622157851061e-05 | 10.38% | 11.58% | 1.12x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.415156383587549e-05 | 4.0765705224143236e-05 | 7.67% | 8.31% | 1.08x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.7047423113960934e-05 | 3.387796801209406e-05 | 8.56% | 9.36% | 1.09x | ✅ |
| `to_wei_decimals[max]` | 4.30400653915347e-05 | 3.9656843263537944e-05 | 7.86% | 8.53% | 1.09x | ✅ |
| `to_wei_decimals[zero]` | 1.4128395684247333e-05 | 1.0295625601316245e-05 | 27.13% | 37.23% | 1.37x | ✅ |
