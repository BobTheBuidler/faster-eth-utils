#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.181222982936903e-06 | 2.787959975007104e-06 | 33.32% | 49.97% | 1.50x | ✅ |
| `humanize_bytes[empty]` | 1.1927775039186397e-06 | 8.366246133166528e-07 | 29.86% | 42.57% | 1.43x | ✅ |
| `humanize_bytes[long]` | 3.931327341591856e-06 | 2.563204697261071e-06 | 34.80% | 53.38% | 1.53x | ✅ |
| `humanize_bytes[short]` | 1.4946437350190409e-06 | 1.2255014322872423e-06 | 18.01% | 21.96% | 1.22x | ✅ |
| `humanize_hash[32-bytes]` | 4.391502601542725e-06 | 2.7717118303288885e-06 | 36.88% | 58.44% | 1.58x | ✅ |
| `humanize_hash[empty]` | 1.4119363999961158e-06 | 8.720299578411002e-07 | 38.24% | 61.91% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.183987185866725e-06 | 2.5732377710727683e-06 | 38.50% | 62.60% | 1.63x | ✅ |
| `humanize_hash[short]` | 1.7239890833751698e-06 | 1.256455336790651e-06 | 27.12% | 37.21% | 1.37x | ✅ |
| `humanize_hexstr[empty]` | 1.948079794625077e-06 | 6.602616480012921e-07 | 66.11% | 195.05% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.67126271463479e-06 | 2.6177297342874525e-06 | 43.96% | 78.45% | 1.78x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9271544664534354e-06 | 2.1222910131222674e-06 | 45.96% | 85.04% | 1.85x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.686565030281951e-06 | 2.6376801504933975e-06 | 43.72% | 77.68% | 1.78x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.9508872803001285e-06 | 2.1258241118024273e-06 | 46.19% | 85.85% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0832785242601105e-05 | 2.400226187398954e-05 | 22.15% | 28.46% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.726993360734075e-05 | 2.9546978201017906e-05 | 20.72% | 26.14% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 8.708034125363869e-07 | 5.683141983816818e-07 | 34.74% | 53.23% | 1.53x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.764911219278127e-05 | 3.634103510881068e-05 | 23.73% | 31.12% | 1.31x | ✅ |
| `humanize_integer_sequence[single]` | 2.7447441890990162e-05 | 1.9971973681009425e-05 | 27.24% | 37.43% | 1.37x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1172515782702896e-05 | 3.247761577269285e-05 | 21.12% | 26.77% | 1.27x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.63603813118153e-05 | 6.555190110032357e-05 | 1.22% | 1.23% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9090883360641205e-05 | 1.617598076761734e-05 | 15.27% | 18.02% | 1.18x | ✅ |
| `humanize_seconds[negative]` | 2.339773141799929e-05 | 1.3725915072521876e-05 | 41.34% | 70.46% | 1.70x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.742272006707842e-05 | 1.650996100202666e-05 | 39.79% | 66.10% | 1.66x | ✅ |
| `humanize_seconds[one-hour]` | 1.8084475651910544e-05 | 1.4713994911727913e-05 | 18.64% | 22.91% | 1.23x | ✅ |
| `humanize_seconds[one-minute]` | 1.833127278947954e-05 | 1.5234953602671552e-05 | 16.89% | 20.32% | 1.20x | ✅ |
| `humanize_seconds[one-second]` | 1.9181764850266724e-05 | 1.584879094075401e-05 | 17.38% | 21.03% | 1.21x | ✅ |
| `humanize_seconds[zero]` | 8.476858446688612e-07 | 6.890225799370795e-07 | 18.72% | 23.03% | 1.23x | ✅ |
| `humanize_wei[ether]` | 2.691635768828434e-05 | 2.5960553132542328e-05 | 3.55% | 3.68% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.6900708869649157e-05 | 2.5455799768006845e-05 | 5.37% | 5.68% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.6800795990374394e-05 | 2.4944492953454312e-05 | 6.93% | 7.44% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.874274946735666e-06 | 3.584094887167408e-06 | 26.47% | 36.00% | 1.36x | ✅ |
| `is_ipfs_uri[empty]` | 1.8175193828223933e-05 | 1.7971626752583024e-05 | 1.12% | 1.13% | 1.01x | ✅ |
| `is_ipfs_uri[invalid-cid]` | 3.210507031846274e-05 | 3.2579183095949224e-05 | -1.48% | -1.46% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 2.991211971472901e-05 | 3.1000261514723364e-05 | -3.64% | -3.51% | 0.96x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.296391189980105e-05 | 3.2793658871962966e-05 | 0.52% | 0.52% | 1.01x | ✅ |
