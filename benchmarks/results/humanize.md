#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.133441379947364e-06 | 2.4872240600035035e-06 | 39.83% | 66.19% | 1.66x | ✅ |
| `humanize_bytes[empty]` | 1.1021855435315195e-06 | 8.144340276707449e-07 | 26.11% | 35.33% | 1.35x | ✅ |
| `humanize_bytes[long]` | 4.008343685780706e-06 | 2.2810791354768405e-06 | 43.09% | 75.72% | 1.76x | ✅ |
| `humanize_bytes[short]` | 1.468386679808153e-06 | 1.0666483745905738e-06 | 27.36% | 37.66% | 1.38x | ✅ |
| `humanize_hash[32-bytes]` | 4.331572364637498e-06 | 2.4787548398851664e-06 | 42.77% | 74.75% | 1.75x | ✅ |
| `humanize_hash[empty]` | 1.3292754128225654e-06 | 8.414137087375046e-07 | 36.70% | 57.98% | 1.58x | ✅ |
| `humanize_hash[long]` | 4.12758317586734e-06 | 2.304691517545557e-06 | 44.16% | 79.09% | 1.79x | ✅ |
| `humanize_hash[short]` | 1.6674678548784708e-06 | 1.1798979547973453e-06 | 29.24% | 41.32% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.9779686669626856e-06 | 6.357359952628828e-07 | 67.86% | 211.13% | 3.11x | ✅ |
| `humanize_hexstr[short-0x]` | 4.753095408418618e-06 | 2.3525951649291816e-06 | 50.50% | 102.04% | 2.02x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.994292530847751e-06 | 1.9086723472838177e-06 | 52.22% | 109.27% | 2.09x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.811654108914722e-06 | 2.382853283769795e-06 | 50.48% | 101.93% | 2.02x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.01560901883863e-06 | 1.887754555260941e-06 | 52.99% | 112.72% | 2.13x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.081472356215633e-05 | 2.3900554104355012e-05 | 22.44% | 28.93% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.765862871286931e-05 | 2.9606132567270303e-05 | 21.38% | 27.20% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 8.927458508087495e-07 | 6.044889426676353e-07 | 32.29% | 47.69% | 1.48x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6091908274026875e-05 | 3.7057081947002916e-05 | 19.60% | 24.38% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.6546271648031532e-05 | 1.9574013576705975e-05 | 26.26% | 35.62% | 1.36x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.127832636427347e-05 | 3.2879585602311985e-05 | 20.35% | 25.54% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.79279330217191e-05 | 6.675264904758212e-05 | 1.73% | 1.76% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9456493913368143e-05 | 1.599853015357521e-05 | 17.77% | 21.61% | 1.22x | ✅ |
| `humanize_seconds[negative]` | 2.3801972717820955e-05 | 1.3514657849981776e-05 | 43.22% | 76.12% | 1.76x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.795271794591562e-05 | 1.5534803262067424e-05 | 44.42% | 79.94% | 1.80x | ✅ |
| `humanize_seconds[one-hour]` | 1.849851183843391e-05 | 1.4472167151530008e-05 | 21.77% | 27.82% | 1.28x | ✅ |
| `humanize_seconds[one-minute]` | 1.8383410219557115e-05 | 1.5296374946743898e-05 | 16.79% | 20.18% | 1.20x | ✅ |
| `humanize_seconds[one-second]` | 1.9463340680070766e-05 | 1.6322553467802714e-05 | 16.14% | 19.24% | 1.19x | ✅ |
| `humanize_seconds[zero]` | 8.086335437303824e-07 | 8.033460167354916e-07 | 0.65% | 0.66% | 1.01x | ✅ |
| `humanize_wei[ether]` | 2.8197434198260582e-05 | 2.6230242347322658e-05 | 6.98% | 7.50% | 1.07x | ✅ |
| `humanize_wei[gwei]` | 2.8677955859063576e-05 | 2.5993951109255e-05 | 9.36% | 10.33% | 1.10x | ✅ |
| `humanize_wei[wei]` | 2.8685555337666278e-05 | 2.565379636279436e-05 | 10.57% | 11.82% | 1.12x | ✅ |
| `humanize_wei[zero]` | 4.774623673355327e-06 | 3.0678042089820827e-06 | 35.75% | 55.64% | 1.56x | ✅ |
| `is_ipfs_uri[empty]` | 1.8123180845062984e-05 | 1.8365468446676057e-05 | -1.34% | -1.32% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.384820778643548e-05 | 3.340597545153307e-05 | 1.31% | 1.32% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.120394331738646e-05 | 3.170678169298472e-05 | -1.61% | -1.59% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.415498638697494e-05 | 3.3862583342249446e-05 | 0.86% | 0.86% | 1.01x | ✅ |
