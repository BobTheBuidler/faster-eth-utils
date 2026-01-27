#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.2557430925631e-06 | 2.5507677352841674e-06 | 40.06% | 66.84% | 1.67x | ✅ |
| `humanize_bytes[empty]` | 1.1084019759887834e-06 | 8.852632388955982e-07 | 20.13% | 25.21% | 1.25x | ✅ |
| `humanize_bytes[long]` | 4.049053034389777e-06 | 2.437554474584506e-06 | 39.80% | 66.11% | 1.66x | ✅ |
| `humanize_bytes[short]` | 1.4555857950439878e-06 | 1.0824907857812512e-06 | 25.63% | 34.47% | 1.34x | ✅ |
| `humanize_hash[32-bytes]` | 4.5214691447427095e-06 | 2.6598312746340394e-06 | 41.17% | 69.99% | 1.70x | ✅ |
| `humanize_hash[empty]` | 1.3482896597085995e-06 | 8.16967919135413e-07 | 39.41% | 65.04% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.289902110128072e-06 | 2.4031544176916048e-06 | 43.98% | 78.51% | 1.79x | ✅ |
| `humanize_hash[short]` | 1.6832607199996534e-06 | 1.0922658496489357e-06 | 35.11% | 54.11% | 1.54x | ✅ |
| `humanize_hexstr[empty]` | 1.8906575980248156e-06 | 6.460408355507669e-07 | 65.83% | 192.65% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.559403041652263e-06 | 2.4257852755384086e-06 | 46.80% | 87.96% | 1.88x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.821506233844567e-06 | 1.982041953645279e-06 | 48.13% | 92.81% | 1.93x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.647093205362148e-06 | 2.3975805576739835e-06 | 48.41% | 93.82% | 1.94x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.856964147421279e-06 | 2.006578797221925e-06 | 47.98% | 92.22% | 1.92x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.090592909132962e-05 | 2.432117441888839e-05 | 21.31% | 27.07% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.688717526291647e-05 | 3.002791424224994e-05 | 18.60% | 22.84% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 9.257453705622376e-07 | 5.662693775197727e-07 | 38.83% | 63.48% | 1.63x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.557810690336287e-05 | 3.750229578596739e-05 | 17.72% | 21.53% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.6763911053321374e-05 | 2.0146086642191058e-05 | 24.73% | 32.85% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0472970899255444e-05 | 3.328070933224172e-05 | 17.77% | 21.61% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.834466380777716e-05 | 6.687901927471184e-05 | 2.14% | 2.19% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9267375721120225e-05 | 1.643291912533553e-05 | 14.71% | 17.25% | 1.17x | ✅ |
| `humanize_seconds[negative]` | 2.4258283009232298e-05 | 1.3765923829143001e-05 | 43.25% | 76.22% | 1.76x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8581957804486422e-05 | 1.638995789905876e-05 | 42.66% | 74.39% | 1.74x | ✅ |
| `humanize_seconds[one-hour]` | 1.833685404901004e-05 | 1.5032580401061375e-05 | 18.02% | 21.98% | 1.22x | ✅ |
| `humanize_seconds[one-minute]` | 1.902316352218022e-05 | 1.580485212387271e-05 | 16.92% | 20.36% | 1.20x | ✅ |
| `humanize_seconds[one-second]` | 1.950505983088054e-05 | 1.644294261451459e-05 | 15.70% | 18.62% | 1.19x | ✅ |
| `humanize_seconds[zero]` | 9.094981341021099e-07 | 7.036412524850906e-07 | 22.63% | 29.26% | 1.29x | ✅ |
| `humanize_wei[ether]` | 2.7026305773757993e-05 | 2.616650998881661e-05 | 3.18% | 3.29% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.697374557299514e-05 | 2.59338382850975e-05 | 3.86% | 4.01% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.679824464259036e-05 | 2.5408201872314578e-05 | 5.19% | 5.47% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.755245423633066e-06 | 3.536996417791595e-06 | 25.62% | 34.44% | 1.34x | ✅ |
| `is_ipfs_uri[empty]` | 1.854845975606271e-05 | 1.888134832957394e-05 | -1.79% | -1.76% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3705001308481504e-05 | 3.320865859374701e-05 | 1.47% | 1.49% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.151362139728433e-05 | 3.109634396628373e-05 | 1.32% | 1.34% | 1.01x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 3.424931278666216e-05 | 3.3635904383704e-05 | 1.79% | 1.82% | 1.02x | ✅ |
