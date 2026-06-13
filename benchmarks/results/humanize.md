#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/benchmark-ci-compiled-wheel-20260314232900/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.121794913114404e-06 | 2.7251252128676725e-06 | 33.88% | 51.25% | 1.51x | ✅ |
| `humanize_bytes[empty]` | 1.2107307830257996e-06 | 8.475965421382649e-07 | 29.99% | 42.84% | 1.43x | ✅ |
| `humanize_bytes[long]` | 3.9599603146298995e-06 | 2.537527057388971e-06 | 35.92% | 56.06% | 1.56x | ✅ |
| `humanize_bytes[short]` | 1.528397312285286e-06 | 1.2016341879970674e-06 | 21.38% | 27.19% | 1.27x | ✅ |
| `humanize_hash[32-bytes]` | 4.394458110865651e-06 | 2.816814915112588e-06 | 35.90% | 56.01% | 1.56x | ✅ |
| `humanize_hash[empty]` | 1.411013801189176e-06 | 8.637592687121657e-07 | 38.78% | 63.36% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.191942919251673e-06 | 2.642525243997702e-06 | 36.96% | 58.63% | 1.59x | ✅ |
| `humanize_hash[short]` | 1.736267773427823e-06 | 1.3425889282482835e-06 | 22.67% | 29.32% | 1.29x | ✅ |
| `humanize_hexstr[empty]` | 1.9416804397460356e-06 | 6.52364232402878e-07 | 66.40% | 197.64% | 2.98x | ✅ |
| `humanize_hexstr[short-0x]` | 4.7021946553724356e-06 | 2.484383288288781e-06 | 47.17% | 89.27% | 1.89x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.027047782103672e-06 | 2.086799636264337e-06 | 48.18% | 92.98% | 1.93x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.759497834550682e-06 | 2.527276284530486e-06 | 46.90% | 88.33% | 1.88x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.961777232157151e-06 | 2.2257878142628826e-06 | 43.82% | 77.99% | 1.78x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.12387705819733e-05 | 2.37219312569552e-05 | 24.06% | 31.69% | 1.32x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.686309843646464e-05 | 2.8601073321633558e-05 | 22.41% | 28.89% | 1.29x | ✅ |
| `humanize_integer_sequence[empty]` | 8.858796387071754e-07 | 5.727933350849538e-07 | 35.34% | 54.66% | 1.55x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5937574486727874e-05 | 3.622039844012068e-05 | 21.15% | 26.83% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.635746990813097e-05 | 1.9929165768596924e-05 | 24.39% | 32.26% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0716411479188546e-05 | 3.255793922078327e-05 | 20.04% | 25.06% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.76275998786989e-05 | 6.571583703015067e-05 | 2.83% | 2.91% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.875555534381554e-05 | 1.596937163010052e-05 | 14.86% | 17.45% | 1.17x | ✅ |
| `humanize_seconds[negative]` | 2.3303895575125293e-05 | 1.3517323174504213e-05 | 42.00% | 72.40% | 1.72x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.6887218983718157e-05 | 1.5813717693743373e-05 | 41.19% | 70.02% | 1.70x | ✅ |
| `humanize_seconds[one-hour]` | 1.787248659504819e-05 | 1.4700344083738391e-05 | 17.75% | 21.58% | 1.22x | ✅ |
| `humanize_seconds[one-minute]` | 1.800969292314225e-05 | 1.5300117138416696e-05 | 15.05% | 17.71% | 1.18x | ✅ |
| `humanize_seconds[one-second]` | 1.8684711064631444e-05 | 1.591636755916284e-05 | 14.82% | 17.39% | 1.17x | ✅ |
| `humanize_seconds[zero]` | 8.234192195015921e-07 | 7.943360414412881e-07 | 3.53% | 3.66% | 1.04x | ✅ |
| `humanize_wei[ether]` | 2.7043798548441173e-05 | 2.6155276308447855e-05 | 3.29% | 3.40% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.714088495262462e-05 | 2.5400932306748815e-05 | 6.41% | 6.85% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.6688813425619182e-05 | 2.5185766153249554e-05 | 5.63% | 5.97% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.8661280358958195e-06 | 3.632691856126711e-06 | 25.35% | 33.95% | 1.34x | ✅ |
| `is_ipfs_uri[empty]` | 1.8347024872227266e-05 | 1.8588530066080515e-05 | -1.32% | -1.30% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.215700596177e-05 | 3.2519480945395446e-05 | -1.13% | -1.11% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.018823028809813e-05 | 3.064747359943693e-05 | -1.52% | -1.50% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.298048899165125e-05 | 3.276613347213872e-05 | 0.65% | 0.65% | 1.01x | ✅ |
