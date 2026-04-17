#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.270510573507918e-06 | 2.594014224282789e-06 | 39.26% | 64.63% | 1.65x | ✅ |
| `humanize_bytes[empty]` | 1.148101557669115e-06 | 8.337331995642766e-07 | 27.38% | 37.71% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.006521155970539e-06 | 2.4074933693320587e-06 | 39.91% | 66.42% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4918256939543325e-06 | 1.0947894625037883e-06 | 26.61% | 36.27% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.6545268983956855e-06 | 2.6234294476625334e-06 | 43.64% | 77.42% | 1.77x | ✅ |
| `humanize_hash[empty]` | 1.3581998073663312e-06 | 8.445363945902711e-07 | 37.82% | 60.82% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.228974482486413e-06 | 2.4234025965128586e-06 | 42.70% | 74.51% | 1.75x | ✅ |
| `humanize_hash[short]` | 1.6879559259755447e-06 | 1.1326341209633967e-06 | 32.90% | 49.03% | 1.49x | ✅ |
| `humanize_hexstr[empty]` | 1.9017035337564016e-06 | 6.643291806800256e-07 | 65.07% | 186.26% | 2.86x | ✅ |
| `humanize_hexstr[short-0x]` | 4.7651233910800465e-06 | 2.489992925568994e-06 | 47.75% | 91.37% | 1.91x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.913093503515199e-06 | 2.0897779841374595e-06 | 46.60% | 87.25% | 1.87x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.7060709088545085e-06 | 2.5900229673987227e-06 | 44.96% | 81.70% | 1.82x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.89686406746526e-06 | 2.110842771760527e-06 | 45.83% | 84.61% | 1.85x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0282242746219395e-05 | 2.455216542931473e-05 | 18.92% | 23.34% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.615011218052859e-05 | 2.9981214032441574e-05 | 17.06% | 20.58% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 8.58308383433337e-07 | 5.722247211698099e-07 | 33.33% | 49.99% | 1.50x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.556155826259022e-05 | 3.7676521511440874e-05 | 17.31% | 20.93% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.6240154159607642e-05 | 2.0281263062045174e-05 | 22.71% | 29.38% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.031286405434119e-05 | 3.347918452921873e-05 | 16.95% | 20.41% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.840325388056451e-05 | 6.75941140432021e-05 | 1.18% | 1.20% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.878923858978071e-05 | 1.6043728539290817e-05 | 14.61% | 17.11% | 1.17x | ✅ |
| `humanize_seconds[negative]` | 2.344151532339651e-05 | 1.3539148107722437e-05 | 42.24% | 73.14% | 1.73x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7580362458585285e-05 | 1.6048026491144384e-05 | 41.81% | 71.86% | 1.72x | ✅ |
| `humanize_seconds[one-hour]` | 1.7840517757882848e-05 | 1.464935400110405e-05 | 17.89% | 21.78% | 1.22x | ✅ |
| `humanize_seconds[one-minute]` | 1.7982126091812977e-05 | 1.5362190545834177e-05 | 14.57% | 17.05% | 1.17x | ✅ |
| `humanize_seconds[one-second]` | 1.89250749356418e-05 | 1.596510810348339e-05 | 15.64% | 18.54% | 1.19x | ✅ |
| `humanize_seconds[zero]` | 8.678063806967284e-07 | 8.206714396004796e-07 | 5.43% | 5.74% | 1.06x | ✅ |
| `humanize_wei[ether]` | 2.6870604391592606e-05 | 2.5549965877774963e-05 | 4.91% | 5.17% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.6842831775834744e-05 | 2.5340518913416337e-05 | 5.60% | 5.93% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.6743610651595758e-05 | 2.478597639788925e-05 | 7.32% | 7.90% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.858526312709688e-06 | 3.2508263325410818e-06 | 33.09% | 49.46% | 1.49x | ✅ |
| `is_ipfs_uri[empty]` | 1.8049239020215586e-05 | 1.910104934029066e-05 | -5.83% | -5.51% | 0.94x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.300901541744782e-05 | 3.3480496472044565e-05 | -1.43% | -1.41% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.066883523278912e-05 | 3.1631435309945814e-05 | -3.14% | -3.04% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.362205453996968e-05 | 3.392099218488492e-05 | -0.89% | -0.88% | 0.99x | ❌ |
