#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.025666989105733e-06 | 2.6282821006963256e-06 | 34.71% | 53.17% | 1.53x | ✅ |
| `humanize_bytes[empty]` | 1.0980358898988813e-06 | 8.418211382581069e-07 | 23.33% | 30.44% | 1.30x | ✅ |
| `humanize_bytes[long]` | 3.83037091347511e-06 | 2.4359379122621255e-06 | 36.40% | 57.24% | 1.57x | ✅ |
| `humanize_bytes[short]` | 1.5254867050284387e-06 | 1.1260805612193934e-06 | 26.18% | 35.47% | 1.35x | ✅ |
| `humanize_hash[32-bytes]` | 4.463435777103683e-06 | 2.6001690552516143e-06 | 41.75% | 71.66% | 1.72x | ✅ |
| `humanize_hash[empty]` | 1.3900095768509677e-06 | 8.318301944028525e-07 | 40.16% | 67.10% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.233858921666913e-06 | 2.3798021822954563e-06 | 43.79% | 77.91% | 1.78x | ✅ |
| `humanize_hash[short]` | 1.7549009819797761e-06 | 1.1319145210360006e-06 | 35.50% | 55.04% | 1.55x | ✅ |
| `humanize_hexstr[empty]` | 2.181080839404152e-06 | 7.079525698385365e-07 | 67.54% | 208.08% | 3.08x | ✅ |
| `humanize_hexstr[short-0x]` | 4.958975688899738e-06 | 2.211336117179808e-06 | 55.41% | 124.25% | 2.24x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.134601234631414e-06 | 1.8321413394281099e-06 | 55.69% | 125.67% | 2.26x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.9176308348897e-06 | 2.364897567355763e-06 | 51.91% | 107.94% | 2.08x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.173592609147393e-06 | 1.8157243486586889e-06 | 56.49% | 129.86% | 2.30x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9714670452434365e-05 | 2.3946237503683408e-05 | 19.41% | 24.09% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.53502205534836e-05 | 2.9139366260203024e-05 | 17.57% | 21.31% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 8.621366505766552e-07 | 6.529155615637474e-07 | 24.27% | 32.04% | 1.32x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.410212297031839e-05 | 3.6423298019204685e-05 | 17.41% | 21.08% | 1.21x | ✅ |
| `humanize_integer_sequence[single]` | 2.621480232810572e-05 | 1.9558176685122128e-05 | 25.39% | 34.04% | 1.34x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.846828656431521e-05 | 3.213082533747278e-05 | 16.47% | 19.72% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 3.606427861495895e-05 | 3.300898800077102e-05 | 8.47% | 9.26% | 1.09x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 2.013524260165017e-05 | 1.844222127434128e-05 | 8.41% | 9.18% | 1.09x | ✅ |
| `humanize_seconds[negative]` | 2.6756229210759764e-05 | 1.8214054147423326e-05 | 31.93% | 46.90% | 1.47x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 3.187077274234875e-05 | 2.0369932620709193e-05 | 36.09% | 56.46% | 1.56x | ✅ |
| `humanize_seconds[one-hour]` | 1.9373565913831024e-05 | 1.79447353482457e-05 | 7.38% | 7.96% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.9324286079802093e-05 | 1.7934585162920924e-05 | 7.19% | 7.75% | 1.08x | ✅ |
| `humanize_seconds[one-second]` | 2.0102888357768083e-05 | 1.8394338850637193e-05 | 8.50% | 9.29% | 1.09x | ✅ |
| `humanize_seconds[zero]` | 1.2745652416776345e-06 | 1.0106143395068363e-06 | 20.71% | 26.12% | 1.26x | ✅ |
| `humanize_wei[ether]` | 2.701912664855757e-05 | 2.590235347999359e-05 | 4.13% | 4.31% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.6923903300556238e-05 | 2.5325237956320974e-05 | 5.94% | 6.31% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.6366385191986626e-05 | 2.4749599080410106e-05 | 6.13% | 6.53% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.662585506984462e-06 | 3.973024766662598e-06 | 14.79% | 17.36% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.3873954004717037e-05 | 1.3924901999406177e-05 | -0.37% | -0.37% | 1.00x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 1.7498525572091562e-05 | 1.6468498603557593e-05 | 5.89% | 6.25% | 1.06x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 1.452417281814604e-05 | 1.466158209323769e-05 | -0.95% | -0.94% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 1.8032192197292342e-05 | 1.655811531022119e-05 | 8.17% | 8.90% | 1.09x | ✅ |
