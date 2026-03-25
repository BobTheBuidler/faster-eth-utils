#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.123408204375904e-06 | 2.7915133616329576e-06 | 32.30% | 47.71% | 1.48x | ✅ |
| `humanize_bytes[empty]` | 1.1929619192847925e-06 | 8.138061172087024e-07 | 31.78% | 46.59% | 1.47x | ✅ |
| `humanize_bytes[long]` | 3.956828468984729e-06 | 2.5741551975458736e-06 | 34.94% | 53.71% | 1.54x | ✅ |
| `humanize_bytes[short]` | 1.4851553177744289e-06 | 1.293354180357031e-06 | 12.91% | 14.83% | 1.15x | ✅ |
| `humanize_hash[32-bytes]` | 4.383007979710791e-06 | 2.740365906066698e-06 | 37.48% | 59.94% | 1.60x | ✅ |
| `humanize_hash[empty]` | 1.367990784038493e-06 | 8.52921376818244e-07 | 37.65% | 60.39% | 1.60x | ✅ |
| `humanize_hash[long]` | 4.176706377098455e-06 | 2.6068958841233605e-06 | 37.58% | 60.22% | 1.60x | ✅ |
| `humanize_hash[short]` | 1.7086982604564664e-06 | 1.242958626792117e-06 | 27.26% | 37.47% | 1.37x | ✅ |
| `humanize_hexstr[empty]` | 1.9403028161207517e-06 | 6.463237443903918e-07 | 66.69% | 200.21% | 3.00x | ✅ |
| `humanize_hexstr[short-0x]` | 4.6873139067413065e-06 | 2.5297410110794347e-06 | 46.03% | 85.29% | 1.85x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.968173111480011e-06 | 2.1256249601650168e-06 | 46.43% | 86.68% | 1.87x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.679382350563154e-06 | 2.5527239686770443e-06 | 45.45% | 83.31% | 1.83x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.966153630916168e-06 | 2.134632939385509e-06 | 46.18% | 85.80% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.043763180129848e-05 | 2.400959495860764e-05 | 21.12% | 26.77% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.636855903650561e-05 | 2.8646596146720045e-05 | 21.23% | 26.96% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.297536790081188e-07 | 5.63744390750966e-07 | 39.37% | 64.92% | 1.65x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.600168172996134e-05 | 3.611361980308974e-05 | 21.50% | 27.38% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.64127202855445e-05 | 2.0528699309997656e-05 | 22.28% | 28.66% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.011974037367687e-05 | 3.214690643504962e-05 | 19.87% | 24.80% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.640986652255912e-05 | 6.573687474179955e-05 | 1.01% | 1.02% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8804717599347774e-05 | 1.589361714118595e-05 | 15.48% | 18.32% | 1.18x | ✅ |
| `humanize_seconds[negative]` | 2.321955874498889e-05 | 1.382946734680631e-05 | 40.44% | 67.90% | 1.68x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7315896186624024e-05 | 1.6055034324178497e-05 | 41.22% | 70.14% | 1.70x | ✅ |
| `humanize_seconds[one-hour]` | 1.8059485992884748e-05 | 1.4675918186560203e-05 | 18.74% | 23.06% | 1.23x | ✅ |
| `humanize_seconds[one-minute]` | 1.8312620959372585e-05 | 1.53518149183168e-05 | 16.17% | 19.29% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.888152178206615e-05 | 1.592173702882697e-05 | 15.68% | 18.59% | 1.19x | ✅ |
| `humanize_seconds[zero]` | 8.169313120340418e-07 | 7.915086751695504e-07 | 3.11% | 3.21% | 1.03x | ✅ |
| `humanize_wei[ether]` | 2.720419889721481e-05 | 2.5992421510378858e-05 | 4.45% | 4.66% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.7214133338465558e-05 | 2.558688765041622e-05 | 5.98% | 6.36% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.7048182798585655e-05 | 2.5274210348374338e-05 | 6.56% | 7.02% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.830245441670901e-06 | 3.6724527417720324e-06 | 23.97% | 31.53% | 1.32x | ✅ |
| `is_ipfs_uri[empty]` | 1.83053562467026e-05 | 1.8539343292565537e-05 | -1.28% | -1.26% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2618247073955315e-05 | 3.2540055841867057e-05 | 0.24% | 0.24% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 2.996385347331038e-05 | 3.0726441543904944e-05 | -2.55% | -2.48% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3187975064662685e-05 | 3.2830472933563164e-05 | 1.08% | 1.09% | 1.01x | ✅ |
