#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.228639504052723e-06 | 2.5367118499750115e-06 | 40.01% | 66.70% | 1.67x | ✅ |
| `humanize_bytes[empty]` | 1.2626857510534887e-06 | 8.511226481258167e-07 | 32.59% | 48.36% | 1.48x | ✅ |
| `humanize_bytes[long]` | 4.063886296197098e-06 | 2.345374221085144e-06 | 42.29% | 73.27% | 1.73x | ✅ |
| `humanize_bytes[short]` | 1.5115943654424562e-06 | 1.0783755684412216e-06 | 28.66% | 40.17% | 1.40x | ✅ |
| `humanize_hash[32-bytes]` | 4.44452250234079e-06 | 2.6032176196855232e-06 | 41.43% | 70.73% | 1.71x | ✅ |
| `humanize_hash[empty]` | 1.4200190947360254e-06 | 8.67730919523992e-07 | 38.89% | 63.65% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.219353282259792e-06 | 2.3607095000600037e-06 | 44.05% | 78.73% | 1.79x | ✅ |
| `humanize_hash[short]` | 1.6905485446153155e-06 | 1.0844580255358557e-06 | 35.85% | 55.89% | 1.56x | ✅ |
| `humanize_hexstr[empty]` | 1.8709811081041919e-06 | 6.85315238701658e-07 | 63.37% | 173.01% | 2.73x | ✅ |
| `humanize_hexstr[short-0x]` | 4.645263086257735e-06 | 2.445177842695148e-06 | 47.36% | 89.98% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.987734767041368e-06 | 1.993022946346964e-06 | 50.02% | 100.08% | 2.00x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.729075399960384e-06 | 2.519306140851862e-06 | 46.73% | 87.71% | 1.88x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.936951808688947e-06 | 1.9802915674823793e-06 | 49.70% | 98.81% | 1.99x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.063471625048157e-05 | 2.3618558222389117e-05 | 22.90% | 29.71% | 1.30x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.660920756053554e-05 | 2.8464056479253515e-05 | 22.25% | 28.62% | 1.29x | ✅ |
| `humanize_integer_sequence[empty]` | 9.245319332156245e-07 | 6.16444709205806e-07 | 33.32% | 49.98% | 1.50x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.4894193115281884e-05 | 3.559418157417791e-05 | 20.72% | 26.13% | 1.26x | ✅ |
| `humanize_integer_sequence[single]` | 2.6827454790420163e-05 | 1.9765902992696785e-05 | 26.32% | 35.73% | 1.36x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0035802183725965e-05 | 3.1696818444632504e-05 | 20.83% | 26.31% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.733292845329939e-05 | 6.62705918787075e-05 | 1.58% | 1.60% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8730450864023537e-05 | 1.691708308805047e-05 | 9.68% | 10.72% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.3806411161463345e-05 | 1.7053317464880868e-05 | 28.37% | 39.60% | 1.40x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7670751063352496e-05 | 1.9056090685793237e-05 | 31.13% | 45.21% | 1.45x | ✅ |
| `humanize_seconds[one-hour]` | 1.742169484531017e-05 | 1.5753159705668066e-05 | 9.58% | 10.59% | 1.11x | ✅ |
| `humanize_seconds[one-minute]` | 1.8099750117628728e-05 | 1.6311033806126173e-05 | 9.88% | 10.97% | 1.11x | ✅ |
| `humanize_seconds[one-second]` | 1.8641470738562164e-05 | 1.6921016003130396e-05 | 9.23% | 10.17% | 1.10x | ✅ |
| `humanize_seconds[zero]` | 8.634474174421141e-07 | 6.459012423932267e-07 | 25.20% | 33.68% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.690370470728749e-05 | 2.643101639835652e-05 | 1.76% | 1.79% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.6817137874857867e-05 | 2.6049123272704088e-05 | 2.86% | 2.95% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.7475070783764806e-05 | 2.557780798890568e-05 | 6.91% | 7.42% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.8142143012401056e-06 | 4.154637886377803e-06 | 13.70% | 15.88% | 1.16x | ✅ |
| `is_ipfs_uri[empty]` | 1.7989346454588193e-05 | 1.8571794251594295e-05 | -3.24% | -3.14% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.261379096013513e-05 | 3.2581670280767554e-05 | 0.10% | 0.10% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0472544647939046e-05 | 3.084654459834825e-05 | -1.23% | -1.21% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.339234285722076e-05 | 3.3287954142190504e-05 | 0.31% | 0.31% | 1.00x | ✅ |
