#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.239037994043929e-06 | 2.6989897363490986e-06 | 36.33% | 57.06% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.1136718089223022e-06 | 9.296526924045786e-07 | 16.52% | 19.79% | 1.20x | ✅ |
| `humanize_bytes[long]` | 4.036954785974768e-06 | 2.5136320161923727e-06 | 37.73% | 60.60% | 1.61x | ✅ |
| `humanize_bytes[short]` | 1.490244986133262e-06 | 1.2630251708408084e-06 | 15.25% | 17.99% | 1.18x | ✅ |
| `humanize_hash[32-bytes]` | 4.476478851657723e-06 | 2.715651741934944e-06 | 39.34% | 64.84% | 1.65x | ✅ |
| `humanize_hash[empty]` | 1.3306304572579006e-06 | 8.24941281476264e-07 | 38.00% | 61.30% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.26482697034802e-06 | 2.4939769551618944e-06 | 41.52% | 71.01% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.7063571602471158e-06 | 1.1988092049993464e-06 | 29.74% | 42.34% | 1.42x | ✅ |
| `humanize_hexstr[empty]` | 1.9212047783509678e-06 | 6.428003769646337e-07 | 66.54% | 198.88% | 2.99x | ✅ |
| `humanize_hexstr[short-0x]` | 4.574264992153218e-06 | 2.4890504629385092e-06 | 45.59% | 83.78% | 1.84x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.839206008508913e-06 | 2.0328861843516655e-06 | 47.05% | 88.85% | 1.89x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.7111343490056655e-06 | 2.4893239492692137e-06 | 47.16% | 89.25% | 1.89x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.825432783046541e-06 | 1.9962274761235895e-06 | 47.82% | 91.63% | 1.92x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0344439647054656e-05 | 2.4664804840547676e-05 | 18.72% | 23.03% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6946425933875614e-05 | 2.9978425838864367e-05 | 18.86% | 23.24% | 1.23x | ✅ |
| `humanize_integer_sequence[empty]` | 9.168836116035223e-07 | 5.708228155230826e-07 | 37.74% | 60.62% | 1.61x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.55817335059439e-05 | 3.9596561023770055e-05 | 13.13% | 15.12% | 1.15x | ✅ |
| `humanize_integer_sequence[single]` | 2.6293420632624273e-05 | 2.009826143451537e-05 | 23.56% | 30.82% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0424614283892576e-05 | 3.329527625531355e-05 | 17.64% | 21.41% | 1.21x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 7.028240688460491e-05 | 6.58261666087879e-05 | 6.34% | 6.77% | 1.07x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8980001835872486e-05 | 1.8289952584987816e-05 | 3.64% | 3.77% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.3932767883307274e-05 | 1.7758953927793055e-05 | 25.80% | 34.76% | 1.35x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7501962203459545e-05 | 2.030484840976342e-05 | 26.17% | 35.45% | 1.35x | ✅ |
| `humanize_seconds[one-hour]` | 1.810428508327016e-05 | 1.6794401936176296e-05 | 7.24% | 7.80% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.823892727995733e-05 | 1.7578723377246443e-05 | 3.62% | 3.76% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.9089989030093734e-05 | 1.9716669310554966e-05 | -3.28% | -3.18% | 0.97x | ❌ |
| `humanize_seconds[zero]` | 8.495302903333828e-07 | 7.01136343499331e-07 | 17.47% | 21.16% | 1.21x | ✅ |
| `humanize_wei[ether]` | 2.78348116921324e-05 | 2.6555906115260805e-05 | 4.59% | 4.82% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.747707888534464e-05 | 2.6122764360707915e-05 | 4.93% | 5.18% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.7335796784767836e-05 | 2.5882179396532972e-05 | 5.32% | 5.62% | 1.06x | ✅ |
| `humanize_wei[zero]` | 5.006125966474987e-06 | 3.6956782548602125e-06 | 26.18% | 35.46% | 1.35x | ✅ |
| `is_ipfs_uri[empty]` | 1.918198932850556e-05 | 1.900057408151305e-05 | 0.95% | 0.95% | 1.01x | ✅ |
| `is_ipfs_uri[invalid-cid]` | 3.412500365054769e-05 | 3.284242598539e-05 | 3.76% | 3.91% | 1.04x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.2156931547481164e-05 | 3.150481581253692e-05 | 2.03% | 2.07% | 1.02x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 3.483716941479304e-05 | 3.357454232387855e-05 | 3.62% | 3.76% | 1.04x | ✅ |
