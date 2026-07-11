#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.125852973834919e-06 | 2.5012139467653466e-06 | 39.38% | 64.95% | 1.65x | ✅ |
| `humanize_bytes[empty]` | 1.045940816263452e-06 | 8.572095030179467e-07 | 18.04% | 22.02% | 1.22x | ✅ |
| `humanize_bytes[long]` | 3.965474809202216e-06 | 2.3089198846908356e-06 | 41.77% | 71.75% | 1.72x | ✅ |
| `humanize_bytes[short]` | 1.4504039095497377e-06 | 1.1629622775398414e-06 | 19.82% | 24.72% | 1.25x | ✅ |
| `humanize_hash[32-bytes]` | 4.372775485117459e-06 | 2.5220959564273905e-06 | 42.32% | 73.38% | 1.73x | ✅ |
| `humanize_hash[empty]` | 1.3189091410343525e-06 | 8.753985806158897e-07 | 33.63% | 50.66% | 1.51x | ✅ |
| `humanize_hash[long]` | 4.1524057278734896e-06 | 2.2958370778558013e-06 | 44.71% | 80.87% | 1.81x | ✅ |
| `humanize_hash[short]` | 1.6490074048472512e-06 | 1.2159003779370794e-06 | 26.26% | 35.62% | 1.36x | ✅ |
| `humanize_hexstr[empty]` | 1.898827637015791e-06 | 6.427434290946999e-07 | 66.15% | 195.43% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.763971013531049e-06 | 2.3242050765485935e-06 | 51.21% | 104.97% | 2.05x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.0002530476423585e-06 | 1.9247880080539097e-06 | 51.88% | 107.83% | 2.08x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.742485686012063e-06 | 2.396649638877661e-06 | 49.46% | 97.88% | 1.98x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.946038255547826e-06 | 1.9218083036914894e-06 | 51.30% | 105.33% | 2.05x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.140599545248786e-05 | 2.3752422265208892e-05 | 24.37% | 32.22% | 1.32x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.741994458813006e-05 | 2.9084365016489726e-05 | 22.28% | 28.66% | 1.29x | ✅ |
| `humanize_integer_sequence[empty]` | 9.196980188306824e-07 | 5.970993113065218e-07 | 35.08% | 54.03% | 1.54x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.657837925274232e-05 | 3.6729151847893946e-05 | 21.15% | 26.82% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.6958115923631658e-05 | 1.95204288102271e-05 | 27.59% | 38.10% | 1.38x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1469322052267855e-05 | 3.24781414538579e-05 | 21.68% | 27.68% | 1.28x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.922197078102773e-05 | 6.714049723815938e-05 | 3.01% | 3.10% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.932915752910936e-05 | 1.5393363665907704e-05 | 20.36% | 25.57% | 1.26x | ✅ |
| `humanize_seconds[negative]` | 2.365017924880328e-05 | 1.2573546099322064e-05 | 46.84% | 88.09% | 1.88x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7781031894536807e-05 | 1.4618584833162905e-05 | 47.38% | 90.04% | 1.90x | ✅ |
| `humanize_seconds[one-hour]` | 1.8186584161841338e-05 | 1.38996610529254e-05 | 23.57% | 30.84% | 1.31x | ✅ |
| `humanize_seconds[one-minute]` | 1.8443192220692318e-05 | 1.4702820378061447e-05 | 20.28% | 25.44% | 1.25x | ✅ |
| `humanize_seconds[one-second]` | 1.919318058215857e-05 | 1.5412469404469613e-05 | 19.70% | 24.53% | 1.25x | ✅ |
| `humanize_seconds[zero]` | 7.664442189276264e-07 | 8.095659867817263e-07 | -5.63% | -5.33% | 0.95x | ❌ |
| `humanize_wei[ether]` | 2.8267370609070118e-05 | 2.641503192083598e-05 | 6.55% | 7.01% | 1.07x | ✅ |
| `humanize_wei[gwei]` | 2.8182024856293228e-05 | 2.588057583392187e-05 | 8.17% | 8.89% | 1.09x | ✅ |
| `humanize_wei[wei]` | 2.8600035495205225e-05 | 2.6211156715477154e-05 | 8.35% | 9.11% | 1.09x | ✅ |
| `humanize_wei[zero]` | 4.649217747437629e-06 | 2.9539362621399813e-06 | 36.46% | 57.39% | 1.57x | ✅ |
| `is_ipfs_uri[empty]` | 1.7928852691637803e-05 | 1.834796261049754e-05 | -2.34% | -2.28% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.390483290152324e-05 | 3.328498525219046e-05 | 1.83% | 1.86% | 1.02x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.128646744461511e-05 | 3.176053276653361e-05 | -1.52% | -1.49% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.452559575503215e-05 | 3.3743955517626934e-05 | 2.26% | 2.32% | 1.02x | ✅ |
