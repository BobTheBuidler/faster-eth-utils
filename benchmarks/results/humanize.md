#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.210138512717619e-06 | 2.6249269859841934e-06 | 37.65% | 60.39% | 1.60x | ✅ |
| `humanize_bytes[empty]` | 1.1676632184623091e-06 | 8.790795383896357e-07 | 24.71% | 32.83% | 1.33x | ✅ |
| `humanize_bytes[long]` | 4.03566155558264e-06 | 2.4033238288697618e-06 | 40.45% | 67.92% | 1.68x | ✅ |
| `humanize_bytes[short]` | 1.4724352822472686e-06 | 1.1010188461623484e-06 | 25.22% | 33.73% | 1.34x | ✅ |
| `humanize_hash[32-bytes]` | 4.466802343354582e-06 | 2.6671040676187956e-06 | 40.29% | 67.48% | 1.67x | ✅ |
| `humanize_hash[empty]` | 1.4095336865756347e-06 | 8.736346665894971e-07 | 38.02% | 61.34% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.263168126116276e-06 | 2.445450034114733e-06 | 42.64% | 74.33% | 1.74x | ✅ |
| `humanize_hash[short]` | 1.6964905959232823e-06 | 1.1016329703604127e-06 | 35.06% | 54.00% | 1.54x | ✅ |
| `humanize_hexstr[empty]` | 1.8738988329735428e-06 | 7.480554409028126e-07 | 60.08% | 150.50% | 2.51x | ✅ |
| `humanize_hexstr[short-0x]` | 4.666342056093654e-06 | 2.4062241483967556e-06 | 48.43% | 93.93% | 1.94x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.945404214939218e-06 | 1.9672999997941725e-06 | 50.14% | 100.55% | 2.01x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.674180642360564e-06 | 2.4288970168512545e-06 | 48.04% | 92.44% | 1.92x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.9009632103598295e-06 | 1.997929804838226e-06 | 48.78% | 95.25% | 1.95x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.083089823280103e-05 | 2.4130490582388726e-05 | 21.73% | 27.77% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.701134737390403e-05 | 2.866384590643144e-05 | 22.55% | 29.12% | 1.29x | ✅ |
| `humanize_integer_sequence[empty]` | 9.401400230614083e-07 | 6.371181834267625e-07 | 32.23% | 47.56% | 1.48x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.510611731090728e-05 | 3.568089157986619e-05 | 20.90% | 26.42% | 1.26x | ✅ |
| `humanize_integer_sequence[single]` | 2.6893596648116294e-05 | 1.9688231991616356e-05 | 26.79% | 36.60% | 1.37x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.021378645028901e-05 | 3.218133819969251e-05 | 19.97% | 24.96% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.805464362926304e-05 | 6.655395818725144e-05 | 2.21% | 2.25% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9075523323624215e-05 | 1.717246397750851e-05 | 9.98% | 11.08% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.377937118534387e-05 | 1.7269485929988407e-05 | 27.38% | 37.70% | 1.38x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.76436761392027e-05 | 1.929391168829316e-05 | 30.20% | 43.28% | 1.43x | ✅ |
| `humanize_seconds[one-hour]` | 1.783149734706863e-05 | 1.5939461883113222e-05 | 10.61% | 11.87% | 1.12x | ✅ |
| `humanize_seconds[one-minute]` | 1.8306483976231413e-05 | 1.6663617381870195e-05 | 8.97% | 9.86% | 1.10x | ✅ |
| `humanize_seconds[one-second]` | 1.8927686677962603e-05 | 1.7134056978012673e-05 | 9.48% | 10.47% | 1.10x | ✅ |
| `humanize_seconds[zero]` | 8.760405729555849e-07 | 7.802054106179593e-07 | 10.94% | 12.28% | 1.12x | ✅ |
| `humanize_wei[ether]` | 2.7760942010242938e-05 | 2.7139802100335795e-05 | 2.24% | 2.29% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.7269193825648686e-05 | 2.6675275925605536e-05 | 2.18% | 2.23% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.713002395795813e-05 | 2.6442672204672674e-05 | 2.53% | 2.60% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.85142525727633e-06 | 4.148501027240613e-06 | 14.49% | 16.94% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.8255275690270465e-05 | 1.8958290311693776e-05 | -3.85% | -3.71% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2816669189552085e-05 | 3.2804726084276904e-05 | 0.04% | 0.04% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.058935353780034e-05 | 3.097703435692827e-05 | -1.27% | -1.25% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.375634732534481e-05 | 3.3410082133870276e-05 | 1.03% | 1.04% | 1.01x | ✅ |
