#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.212719473112404e-06 | 2.691217438395485e-06 | 36.12% | 56.54% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.135683798916761e-06 | 8.225123752622457e-07 | 27.58% | 38.07% | 1.38x | ✅ |
| `humanize_bytes[long]` | 4.0194368369707525e-06 | 2.463055849091942e-06 | 38.72% | 63.19% | 1.63x | ✅ |
| `humanize_bytes[short]` | 1.48354640170706e-06 | 1.132940993753802e-06 | 23.63% | 30.95% | 1.31x | ✅ |
| `humanize_hash[32-bytes]` | 4.468908893687425e-06 | 2.666196883459363e-06 | 40.34% | 67.61% | 1.68x | ✅ |
| `humanize_hash[empty]` | 1.360322569620672e-06 | 8.145689452307368e-07 | 40.12% | 67.00% | 1.67x | ✅ |
| `humanize_hash[long]` | 4.255942575204503e-06 | 2.4601195921386427e-06 | 42.20% | 73.00% | 1.73x | ✅ |
| `humanize_hash[short]` | 1.7195593492659612e-06 | 1.1177845591005857e-06 | 35.00% | 53.84% | 1.54x | ✅ |
| `humanize_hexstr[empty]` | 1.880647498229532e-06 | 6.281734431990288e-07 | 66.60% | 199.38% | 2.99x | ✅ |
| `humanize_hexstr[short-0x]` | 4.514550629371971e-06 | 2.5663472023922464e-06 | 43.15% | 75.91% | 1.76x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.75880797690911e-06 | 2.0336074880012637e-06 | 45.90% | 84.83% | 1.85x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.63606792733368e-06 | 2.6285884095964246e-06 | 43.30% | 76.37% | 1.76x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.788625907110737e-06 | 2.039712556055995e-06 | 46.16% | 85.74% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0246021423110588e-05 | 2.44678328458915e-05 | 19.10% | 23.62% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.657912920881916e-05 | 3.0266823354664888e-05 | 17.26% | 20.86% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 8.939059205106563e-07 | 5.688935168727896e-07 | 36.36% | 57.13% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.612795587459384e-05 | 3.7927056323653645e-05 | 17.78% | 21.62% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.628934772089563e-05 | 2.0469197935361572e-05 | 22.14% | 28.43% | 1.28x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0259571413949905e-05 | 3.383246945823795e-05 | 15.96% | 19.00% | 1.19x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.815561614456842e-05 | 6.764840071026441e-05 | 0.74% | 0.75% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.909083593407819e-05 | 1.8475420038926376e-05 | 3.22% | 3.33% | 1.03x | ✅ |
| `humanize_seconds[negative]` | 2.4678458204376554e-05 | 1.7806292879084007e-05 | 27.85% | 38.59% | 1.39x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8765009179845384e-05 | 2.0321695027432736e-05 | 29.35% | 41.55% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.8025878535211855e-05 | 1.703319913292573e-05 | 5.51% | 5.83% | 1.06x | ✅ |
| `humanize_seconds[one-minute]` | 1.8378091385883872e-05 | 1.770637216306079e-05 | 3.65% | 3.79% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.8994047015559616e-05 | 1.8297684829155042e-05 | 3.67% | 3.81% | 1.04x | ✅ |
| `humanize_seconds[zero]` | 8.65387063621334e-07 | 6.749539195949653e-07 | 22.01% | 28.21% | 1.28x | ✅ |
| `humanize_wei[ether]` | 2.7535381521870672e-05 | 2.665650610593297e-05 | 3.19% | 3.30% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.7003502291346878e-05 | 2.592064165260589e-05 | 4.01% | 4.18% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.7202997353008877e-05 | 2.5462524825646908e-05 | 6.40% | 6.84% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.758711579981831e-06 | 3.6407023308205635e-06 | 23.49% | 30.71% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.8272305402835207e-05 | 1.9826979042733203e-05 | -8.51% | -7.84% | 0.92x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.288372860579023e-05 | 3.319901926026898e-05 | -0.96% | -0.95% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.1209291677774556e-05 | 3.16752281416459e-05 | -1.49% | -1.47% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.358141843832673e-05 | 3.325847983369972e-05 | 0.96% | 0.97% | 1.01x | ✅ |
