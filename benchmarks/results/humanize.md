#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.277822781746958e-06 | 2.7702625975801398e-06 | 35.24% | 54.42% | 1.54x | ✅ |
| `humanize_bytes[empty]` | 1.1708406445355672e-06 | 8.180911615769112e-07 | 30.13% | 43.12% | 1.43x | ✅ |
| `humanize_bytes[long]` | 4.084738670918232e-06 | 2.5660478694955405e-06 | 37.18% | 59.18% | 1.59x | ✅ |
| `humanize_bytes[short]` | 1.5253289253456638e-06 | 1.1151243049245034e-06 | 26.89% | 36.79% | 1.37x | ✅ |
| `humanize_hash[32-bytes]` | 4.518932827884498e-06 | 2.7883778836994135e-06 | 38.30% | 62.06% | 1.62x | ✅ |
| `humanize_hash[empty]` | 1.3619516163942075e-06 | 8.329129647912051e-07 | 38.84% | 63.52% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.32967607863144e-06 | 2.5923633442032985e-06 | 40.13% | 67.02% | 1.67x | ✅ |
| `humanize_hash[short]` | 1.753069542935867e-06 | 1.2672719828891808e-06 | 27.71% | 38.33% | 1.38x | ✅ |
| `humanize_hexstr[empty]` | 1.9022292517517404e-06 | 6.375845216069581e-07 | 66.48% | 198.35% | 2.98x | ✅ |
| `humanize_hexstr[short-0x]` | 4.723379279959358e-06 | 2.4883495001213586e-06 | 47.32% | 89.82% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9674371571554885e-06 | 2.0821285147827883e-06 | 47.52% | 90.55% | 1.91x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.826361639912618e-06 | 2.463579615993496e-06 | 48.96% | 95.91% | 1.96x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.961716265973058e-06 | 2.043135898676129e-06 | 48.43% | 93.90% | 1.94x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.019143003040818e-05 | 2.4501472154043244e-05 | 18.85% | 23.22% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6889097935130036e-05 | 2.965259541088706e-05 | 19.62% | 24.40% | 1.24x | ✅ |
| `humanize_integer_sequence[empty]` | 8.898939251541395e-07 | 5.864163765518067e-07 | 34.10% | 51.75% | 1.52x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.530340187759148e-05 | 3.7087667050376834e-05 | 18.13% | 22.15% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.6335778244620743e-05 | 2.0251544697477223e-05 | 23.10% | 30.04% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.02019530623741e-05 | 3.285548301480311e-05 | 18.27% | 22.36% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.872041540332772e-05 | 6.864350975778884e-05 | 0.11% | 0.11% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.927377571978829e-05 | 1.784932198169009e-05 | 7.39% | 7.98% | 1.08x | ✅ |
| `humanize_seconds[negative]` | 2.39366048219884e-05 | 1.8003035181713977e-05 | 24.79% | 32.96% | 1.33x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7728416017331708e-05 | 1.9891782116615978e-05 | 28.26% | 39.40% | 1.39x | ✅ |
| `humanize_seconds[one-hour]` | 1.8078099692062835e-05 | 1.657118707260836e-05 | 8.34% | 9.09% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.8385771881479175e-05 | 1.7282588355138963e-05 | 6.00% | 6.38% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.9209300594059096e-05 | 1.780558001361263e-05 | 7.31% | 7.88% | 1.08x | ✅ |
| `humanize_seconds[zero]` | 9.030619548425168e-07 | 6.494319035104323e-07 | 28.09% | 39.05% | 1.39x | ✅ |
| `humanize_wei[ether]` | 2.707847226599609e-05 | 2.739601577706262e-05 | -1.17% | -1.16% | 0.99x | ❌ |
| `humanize_wei[gwei]` | 2.699899481919e-05 | 2.648985438008117e-05 | 1.89% | 1.92% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.682077333979453e-05 | 2.611651283560191e-05 | 2.63% | 2.70% | 1.03x | ✅ |
| `humanize_wei[zero]` | 5.003956243365758e-06 | 4.320589483982057e-06 | 13.66% | 15.82% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.8810887397410946e-05 | 1.9288627372755382e-05 | -2.54% | -2.48% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.345402152262802e-05 | 3.414473356857702e-05 | -2.06% | -2.02% | 0.98x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.134821547044072e-05 | 3.210219417339098e-05 | -2.41% | -2.35% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4041527595894485e-05 | 3.451774304683976e-05 | -1.40% | -1.38% | 0.99x | ❌ |
