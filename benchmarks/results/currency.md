#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.4444150217937127e-05 | 2.551844032259149e-05 | -4.39% | -4.21% | 0.96x | ❌ |
| `from_wei[1-gwei]` | 2.4049307158086156e-05 | 2.5353243560738316e-05 | -5.42% | -5.14% | 0.95x | ❌ |
| `from_wei[max]` | 2.623020761929203e-05 | 2.6567496419272752e-05 | -1.29% | -1.27% | 0.99x | ❌ |
| `from_wei[zero]` | 2.5147837432999234e-06 | 2.6919313380960484e-06 | -7.04% | -6.58% | 0.93x | ❌ |
| `from_wei_decimals[100M-8dec]` | 2.8799155556424234e-05 | 2.913680089891194e-05 | -1.17% | -1.16% | 0.99x | ❌ |
| `from_wei_decimals[max]` | 3.0351496502543826e-05 | 3.138818298962678e-05 | -3.42% | -3.30% | 0.97x | ❌ |
| `from_wei_decimals[zero]` | 7.274753002545368e-06 | 7.501784009037606e-06 | -3.12% | -3.03% | 0.97x | ❌ |
| `to_wei[1-ether]` | 3.2004628184866294e-05 | 2.916916806098896e-05 | 8.86% | 9.72% | 1.10x | ✅ |
| `to_wei[1.5-ether]` | 4.024395160669951e-05 | 3.662347778354149e-05 | 9.00% | 9.89% | 1.10x | ✅ |
| `to_wei[2str-ether]` | 3.2438887264130504e-05 | 2.9784903459243522e-05 | 8.18% | 8.91% | 1.09x | ✅ |
| `to_wei[max]` | 3.810510842680008e-05 | 3.45729405169943e-05 | 9.27% | 10.22% | 1.10x | ✅ |
| `to_wei[zero]` | 9.248219777901356e-06 | 6.629009031484781e-06 | 28.32% | 39.51% | 1.40x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.767252654326975e-05 | 3.321923355638164e-05 | 11.82% | 13.41% | 1.13x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.46917411964761e-05 | 4.088249301412215e-05 | 8.52% | 9.32% | 1.09x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.675219743694253e-05 | 3.414993893094166e-05 | 7.08% | 7.62% | 1.08x | ✅ |
| `to_wei_decimals[max]` | 4.278573265577684e-05 | 3.894793987859335e-05 | 8.97% | 9.85% | 1.10x | ✅ |
| `to_wei_decimals[zero]` | 1.3884529128277353e-05 | 1.0785782381967077e-05 | 22.32% | 28.73% | 1.29x | ✅ |
