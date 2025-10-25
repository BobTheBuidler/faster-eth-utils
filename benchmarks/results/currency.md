#### [faster_eth_utils.currency](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/currency.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_currency_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `from_wei[1-ether]` | 2.423375810968127e-05 | 2.4434639906123566e-05 | -0.83% | -0.82% | 0.99x | ❌ |
| `from_wei[1-gwei]` | 2.3831121408977323e-05 | 2.394474222258e-05 | -0.48% | -0.47% | 1.00x | ❌ |
| `from_wei[max]` | 2.629406023296857e-05 | 2.6145930766559984e-05 | 0.56% | 0.57% | 1.01x | ✅ |
| `from_wei[zero]` | 2.5951817570655938e-06 | 2.8181644866104364e-06 | -8.59% | -7.91% | 0.92x | ❌ |
| `from_wei_decimals[100M-8dec]` | 2.9376957066321744e-05 | 2.850507475405176e-05 | 2.97% | 3.06% | 1.03x | ✅ |
| `from_wei_decimals[max]` | 3.102002686523153e-05 | 3.0372033740942674e-05 | 2.09% | 2.13% | 1.02x | ✅ |
| `from_wei_decimals[zero]` | 7.4584649448528814e-06 | 7.363697925345094e-06 | 1.27% | 1.29% | 1.01x | ✅ |
| `to_wei[1-ether]` | 3.222321199808873e-05 | 3.115291408199012e-05 | 3.32% | 3.44% | 1.03x | ✅ |
| `to_wei[1.5-ether]` | 4.022742448990651e-05 | 3.9341778252731467e-05 | 2.20% | 2.25% | 1.02x | ✅ |
| `to_wei[2str-ether]` | 3.2507837749671655e-05 | 3.202719085548043e-05 | 1.48% | 1.50% | 1.02x | ✅ |
| `to_wei[max]` | 3.8556426086826596e-05 | 3.71235837192771e-05 | 3.72% | 3.86% | 1.04x | ✅ |
| `to_wei[zero]` | 9.432646197957696e-06 | 8.52217053522797e-06 | 9.65% | 10.68% | 1.11x | ✅ |
| `to_wei_decimals[1-8dec]` | 3.753147662877832e-05 | 3.471917250696468e-05 | 7.49% | 8.10% | 1.08x | ✅ |
| `to_wei_decimals[1.5-8dec]` | 4.519619863999959e-05 | 4.3671726917585935e-05 | 3.37% | 3.49% | 1.03x | ✅ |
| `to_wei_decimals[2str-8dec]` | 3.7473432071904146e-05 | 3.5713519479148684e-05 | 4.70% | 4.93% | 1.05x | ✅ |
| `to_wei_decimals[max]` | 4.381397318009649e-05 | 4.1501572161391136e-05 | 5.28% | 5.57% | 1.06x | ✅ |
| `to_wei_decimals[zero]` | 1.3640510862757546e-05 | 1.171449281551288e-05 | 14.12% | 16.44% | 1.16x | ✅ |
