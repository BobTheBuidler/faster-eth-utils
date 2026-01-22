#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.002400052412149e-06 | 2.527032242523647e-06 | 36.86% | 58.38% | 1.58x | ✅ |
| `humanize_bytes[empty]` | 1.1079390046484925e-06 | 8.303119647124722e-07 | 25.06% | 33.44% | 1.33x | ✅ |
| `humanize_bytes[long]` | 3.791852105887829e-06 | 2.4987614208600615e-06 | 34.10% | 51.75% | 1.52x | ✅ |
| `humanize_bytes[short]` | 1.4552921663326892e-06 | 1.0832386469459883e-06 | 25.57% | 34.35% | 1.34x | ✅ |
| `humanize_hash[32-bytes]` | 4.259439842257738e-06 | 2.5696572638846724e-06 | 39.67% | 65.76% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.3375893057081345e-06 | 8.255596766875891e-07 | 38.28% | 62.02% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.061346865043146e-06 | 2.3732190941163366e-06 | 41.57% | 71.13% | 1.71x | ✅ |
| `humanize_hash[short]` | 1.6629431074186481e-06 | 1.0905485450468295e-06 | 34.42% | 52.49% | 1.52x | ✅ |
| `humanize_hexstr[empty]` | 1.782504250823037e-06 | 5.629385512734825e-07 | 68.42% | 216.64% | 3.17x | ✅ |
| `humanize_hexstr[short-0x]` | 4.4498889708381e-06 | 2.17878333411617e-06 | 51.04% | 104.24% | 2.04x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7390514842298027e-06 | 1.7534914496991173e-06 | 53.10% | 113.23% | 2.13x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.55150539964248e-06 | 2.2413722158969375e-06 | 50.76% | 103.07% | 2.03x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.757111996588084e-06 | 1.7594690828731708e-06 | 53.17% | 113.54% | 2.14x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.971288438266125e-05 | 2.1453951071815506e-05 | 27.80% | 38.50% | 1.38x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.4625565286425845e-05 | 2.6380266793319057e-05 | 23.81% | 31.26% | 1.31x | ✅ |
| `humanize_integer_sequence[empty]` | 7.938281394916648e-07 | 5.198210212156741e-07 | 34.52% | 52.71% | 1.53x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.263989683065984e-05 | 3.45017771432727e-05 | 19.09% | 23.59% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.5740032601913693e-05 | 1.85438960498225e-05 | 27.96% | 38.81% | 1.39x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.791208790276576e-05 | 3.018006773791189e-05 | 20.39% | 25.62% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.252601060544989e-05 | 6.357285774214232e-05 | -1.67% | -1.65% | 0.98x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8170221124882992e-05 | 1.624942230666492e-05 | 10.57% | 11.82% | 1.12x | ✅ |
| `humanize_seconds[negative]` | 2.3566051788124432e-05 | 1.5998532947453867e-05 | 32.11% | 47.30% | 1.47x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8072379122546594e-05 | 1.881508128892695e-05 | 32.98% | 49.20% | 1.49x | ✅ |
| `humanize_seconds[one-hour]` | 1.7213753404324864e-05 | 1.5430499623920794e-05 | 10.36% | 11.56% | 1.12x | ✅ |
| `humanize_seconds[one-minute]` | 1.7411066745592502e-05 | 1.5852485069558153e-05 | 8.95% | 9.83% | 1.10x | ✅ |
| `humanize_seconds[one-second]` | 1.8100158053164214e-05 | 1.6409011065755434e-05 | 9.34% | 10.31% | 1.10x | ✅ |
| `humanize_seconds[zero]` | 7.5818949467564e-07 | 5.871387386228743e-07 | 22.56% | 29.13% | 1.29x | ✅ |
| `humanize_wei[ether]` | 2.589867531068705e-05 | 2.4661998141020262e-05 | 4.78% | 5.01% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.5715664815771563e-05 | 2.4078846144319828e-05 | 6.37% | 6.80% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.5320424294517602e-05 | 2.3572714153473263e-05 | 6.90% | 7.41% | 1.07x | ✅ |
| `humanize_wei[zero]` | 4.6158731124439994e-06 | 3.4355682939670743e-06 | 25.57% | 34.36% | 1.34x | ✅ |
| `is_ipfs_uri[empty]` | 1.624873713144306e-05 | 1.6853459871285345e-05 | -3.72% | -3.59% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.027629150810095e-05 | 3.178351251174526e-05 | -4.98% | -4.74% | 0.95x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 2.8196451919547576e-05 | 2.9775921424414662e-05 | -5.60% | -5.30% | 0.95x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.1099760908643936e-05 | 3.237219963764863e-05 | -4.09% | -3.93% | 0.96x | ❌ |
