#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.226543106943365e-06 | 2.6459700154447236e-06 | 37.40% | 59.74% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.0857624678183278e-06 | 7.937323765701545e-07 | 26.90% | 36.79% | 1.37x | ✅ |
| `humanize_bytes[long]` | 4.021873836817105e-06 | 2.4677705788868762e-06 | 38.64% | 62.98% | 1.63x | ✅ |
| `humanize_bytes[short]` | 1.4582564690524555e-06 | 1.079757599643169e-06 | 25.96% | 35.05% | 1.35x | ✅ |
| `humanize_hash[32-bytes]` | 4.4770105177048386e-06 | 2.6393273297143277e-06 | 41.05% | 69.63% | 1.70x | ✅ |
| `humanize_hash[empty]` | 1.3429702710410476e-06 | 9.585172903042282e-07 | 28.63% | 40.11% | 1.40x | ✅ |
| `humanize_hash[long]` | 4.241746912045835e-06 | 2.4760325738627996e-06 | 41.63% | 71.31% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.7053849597994496e-06 | 1.0862475115529564e-06 | 36.30% | 57.00% | 1.57x | ✅ |
| `humanize_hexstr[empty]` | 1.885079831507924e-06 | 6.363485035282873e-07 | 66.24% | 196.23% | 2.96x | ✅ |
| `humanize_hexstr[short-0x]` | 4.490561772797863e-06 | 2.5711704612549158e-06 | 42.74% | 74.65% | 1.75x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7928942943885094e-06 | 2.0372308746572892e-06 | 46.29% | 86.18% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.599675870622603e-06 | 2.543812949246286e-06 | 44.70% | 80.82% | 1.81x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7831751488295007e-06 | 1.9992681663418388e-06 | 47.15% | 89.23% | 1.89x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.080789953869195e-05 | 2.5064470672452885e-05 | 18.64% | 22.91% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.691777935508687e-05 | 3.018210619818288e-05 | 18.25% | 22.32% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 9.122336372591334e-07 | 5.891706638111683e-07 | 35.41% | 54.83% | 1.55x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.558034762009122e-05 | 3.762839538359239e-05 | 17.45% | 21.13% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.6526431878338084e-05 | 2.0133271163940164e-05 | 24.10% | 31.75% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.032307056339969e-05 | 3.350546885437378e-05 | 16.91% | 20.35% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.749192046913592e-05 | 6.72869580417067e-05 | 0.30% | 0.30% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9078604844683422e-05 | 1.8144605924667053e-05 | 4.90% | 5.15% | 1.05x | ✅ |
| `humanize_seconds[negative]` | 2.372668669913254e-05 | 1.749574983925811e-05 | 26.26% | 35.61% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7640353980333828e-05 | 1.994171765651117e-05 | 27.85% | 38.61% | 1.39x | ✅ |
| `humanize_seconds[one-hour]` | 1.792329844399544e-05 | 1.6734219511323834e-05 | 6.63% | 7.11% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.816692082169745e-05 | 1.7412133286829167e-05 | 4.15% | 4.33% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.8867314747236352e-05 | 1.8225074856545264e-05 | 3.40% | 3.52% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.742449357380321e-07 | 7.500105941143237e-07 | 14.21% | 16.56% | 1.17x | ✅ |
| `humanize_wei[ether]` | 2.698016189013799e-05 | 2.6129922871688466e-05 | 3.15% | 3.25% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.6874767223084774e-05 | 2.5686525137257197e-05 | 4.42% | 4.63% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.673206323798568e-05 | 2.544528730940086e-05 | 4.81% | 5.06% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.810252380263828e-06 | 3.6560391143642505e-06 | 23.99% | 31.57% | 1.32x | ✅ |
| `is_ipfs_uri[empty]` | 1.840381605584111e-05 | 1.893455203635766e-05 | -2.88% | -2.80% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3118877402399274e-05 | 3.297805473892602e-05 | 0.43% | 0.43% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.068808587412317e-05 | 3.123390290755856e-05 | -1.78% | -1.75% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.378141922298344e-05 | 3.34818904033921e-05 | 0.89% | 0.89% | 1.01x | ✅ |
