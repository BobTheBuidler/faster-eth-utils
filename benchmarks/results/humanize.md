#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.286203246464375e-06 | 2.7361387704491657e-06 | 36.16% | 56.65% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.1694971343250923e-06 | 8.070991928499142e-07 | 30.99% | 44.90% | 1.45x | ✅ |
| `humanize_bytes[long]` | 4.075811327014443e-06 | 2.4516748085672472e-06 | 39.85% | 66.25% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4994007039804765e-06 | 1.1467782002306558e-06 | 23.52% | 30.75% | 1.31x | ✅ |
| `humanize_hash[32-bytes]` | 4.476379440035989e-06 | 2.6633552529577716e-06 | 40.50% | 68.07% | 1.68x | ✅ |
| `humanize_hash[empty]` | 1.3502724234074066e-06 | 8.082148889836277e-07 | 40.14% | 67.07% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.2687929016187365e-06 | 2.4127718462456283e-06 | 43.48% | 76.92% | 1.77x | ✅ |
| `humanize_hash[short]` | 1.6780982559932262e-06 | 1.316619798129334e-06 | 21.54% | 27.46% | 1.27x | ✅ |
| `humanize_hexstr[empty]` | 1.9061849546095083e-06 | 6.325050313329685e-07 | 66.82% | 201.37% | 3.01x | ✅ |
| `humanize_hexstr[short-0x]` | 4.716766280069768e-06 | 2.410508182719786e-06 | 48.89% | 95.68% | 1.96x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.039230520764779e-06 | 2.0009805894675793e-06 | 50.46% | 101.86% | 2.02x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.682047367404047e-06 | 2.4465200782346946e-06 | 47.75% | 91.38% | 1.91x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.947627887584788e-06 | 1.978172747581178e-06 | 49.89% | 99.56% | 2.00x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.02187883476416e-05 | 2.4230245078935804e-05 | 19.82% | 24.72% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.636670722748411e-05 | 2.9425069405480238e-05 | 19.09% | 23.59% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 8.771701643194139e-07 | 5.584942694606423e-07 | 36.33% | 57.06% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.537490837891905e-05 | 3.7142518376048586e-05 | 18.14% | 22.16% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.6338081334518643e-05 | 2.0192850197129925e-05 | 23.33% | 30.43% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.998653706801598e-05 | 3.293794101549769e-05 | 17.63% | 21.40% | 1.21x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.889860090824271e-05 | 6.877904916501844e-05 | 0.17% | 0.17% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9162410874506236e-05 | 1.8243805495912248e-05 | 4.79% | 5.04% | 1.05x | ✅ |
| `humanize_seconds[negative]` | 2.3777074655329786e-05 | 1.782348492019735e-05 | 25.04% | 33.40% | 1.33x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7807657842807107e-05 | 2.0231157017997122e-05 | 27.25% | 37.45% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.8197755193760034e-05 | 1.67252127051674e-05 | 8.09% | 8.80% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.839834761330644e-05 | 1.7645209731519483e-05 | 4.09% | 4.27% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.901863062236645e-05 | 1.814785175746855e-05 | 4.58% | 4.80% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.887109620800722e-07 | 7.682298050334669e-07 | 13.56% | 15.68% | 1.16x | ✅ |
| `humanize_wei[ether]` | 2.777404074696433e-05 | 2.6585859344499413e-05 | 4.28% | 4.47% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.7117782252554197e-05 | 2.5690571040665816e-05 | 5.26% | 5.56% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.728431676036732e-05 | 2.5982906255718347e-05 | 4.77% | 5.01% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.99361195052543e-06 | 3.668230047398062e-06 | 26.54% | 36.13% | 1.36x | ✅ |
| `is_ipfs_uri[empty]` | 1.8748171416315496e-05 | 1.931164091306335e-05 | -3.01% | -2.92% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.348339083050186e-05 | 3.3871987120288756e-05 | -1.16% | -1.15% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.1110243953224977e-05 | 3.2090814502524135e-05 | -3.15% | -3.06% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.418103419295736e-05 | 3.434770642115848e-05 | -0.49% | -0.49% | 1.00x | ❌ |
