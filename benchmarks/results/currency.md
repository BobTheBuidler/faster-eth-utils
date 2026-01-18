#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.3914635450662272e-05 | 2.385321023849029e-05 | 0.26% | 0.26% | 1.00x | ✅ |
| `from_wei[1-gwei]` | 2.3833320846809106e-05 | 2.348128153316839e-05 | 1.48% | 1.50% | 1.01x | ✅ |
| `from_wei[max]` | 2.5913040722774542e-05 | 2.527320531319979e-05 | 2.47% | 2.53% | 1.03x | ✅ |
| `from_wei[zero]` | 2.5145726754702144e-06 | 1.9903398691144552e-06 | 20.85% | 26.34% | 1.26x | ✅ |
| `from_wei_decimals[100M-8dec]` | 2.869405254899946e-05 | 2.870400004339126e-05 | -0.03% | -0.03% | 1.00x | ❌ |
| `from_wei_decimals[max]` | 3.001502385793447e-05 | 3.0307171315353172e-05 | -0.97% | -0.96% | 0.99x | ❌ |
| `from_wei_decimals[zero]` | 7.336992859863229e-06 | 7.371058556880088e-06 | -0.46% | -0.46% | 1.00x | ❌ |
| `to_wei[1-ether]` | 3.179052863684332e-05 | 2.8637459213258474e-05 | 9.92% | 11.01% | 1.11x | ✅ |
| `to_wei[1.5-ether]` | 3.940564661950731e-05 | 3.635198555202993e-05 | 7.75% | 8.40% | 1.08x | ✅ |
| `to_wei[2str-ether]` | 3.241106342997929e-05 | 2.959039033625246e-05 | 8.70% | 9.53% | 1.10x | ✅ |
| `to_wei[max]` | 3.8141575465881815e-05 | 3.4081441263312397e-05 | 10.64% | 11.91% | 1.12x | ✅ |
| `to_wei[zero]` | 9.290375403124862e-06 | 5.805947063419487e-06 | 37.51% | 60.01% | 1.60x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.7110661783670136e-05 | 3.27696496634051e-05 | 11.70% | 13.25% | 1.13x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.3580173893427076e-05 | 4.043162092262556e-05 | 7.22% | 7.79% | 1.08x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.6074964785333845e-05 | 3.362298096108998e-05 | 6.80% | 7.29% | 1.07x | ✅ |
| `to_wei_decimals[max]` | 4.263648287509415e-05 | 4.07192725899465e-05 | 4.50% | 4.71% | 1.05x | ✅ |
| `to_wei_decimals[zero]` | 1.3436360925882646e-05 | 1.04412777709336e-05 | 22.29% | 28.69% | 1.29x | ✅ |
