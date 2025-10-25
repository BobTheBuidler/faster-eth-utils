#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.190058201652376e-06 | 2.768787660277453e-06 | 33.92% | 51.33% | 1.51x | ✅ |
| `humanize_bytes[empty]` | 1.1724642255535576e-06 | 9.552950332738992e-07 | 18.52% | 22.73% | 1.23x | ✅ |
| `humanize_bytes[long]` | 3.976148243635548e-06 | 2.6767598572685843e-06 | 32.68% | 48.54% | 1.49x | ✅ |
| `humanize_bytes[short]` | 1.49026270369969e-06 | 1.1972854269216163e-06 | 19.66% | 24.47% | 1.24x | ✅ |
| `humanize_hash[32-bytes]` | 4.435190886751432e-06 | 2.8916979284471532e-06 | 34.80% | 53.38% | 1.53x | ✅ |
| `humanize_hash[empty]` | 1.3968213929481416e-06 | 8.792864107666505e-07 | 37.05% | 58.86% | 1.59x | ✅ |
| `humanize_hash[long]` | 4.180540225192019e-06 | 2.67159093684633e-06 | 36.09% | 56.48% | 1.56x | ✅ |
| `humanize_hash[short]` | 1.6697923571840795e-06 | 1.2678395030208404e-06 | 24.07% | 31.70% | 1.32x | ✅ |
| `humanize_hexstr[empty]` | 1.8902051610219016e-06 | 6.767917837975448e-07 | 64.19% | 179.29% | 2.79x | ✅ |
| `humanize_hexstr[short-0x]` | 4.667045772538937e-06 | 2.3915656652171585e-06 | 48.76% | 95.15% | 1.95x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9280364236432826e-06 | 1.9453531651952317e-06 | 50.48% | 101.92% | 2.02x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.711406405946104e-06 | 2.5004296181408297e-06 | 46.93% | 88.42% | 1.88x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.954519910358175e-06 | 2.0059401059709393e-06 | 49.27% | 97.14% | 1.97x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0148880926071537e-05 | 2.3704173359472087e-05 | 21.38% | 27.19% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.611770749175242e-05 | 2.879812271623418e-05 | 20.27% | 25.42% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.229743680905511e-07 | 6.113555224923432e-07 | 33.76% | 50.97% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.4362232456498765e-05 | 3.608833101312539e-05 | 18.65% | 22.93% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.6676491309572348e-05 | 2.066988721040448e-05 | 22.52% | 29.06% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.970027920976985e-05 | 3.2096499767273104e-05 | 19.15% | 23.69% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 7.167637877500692e-05 | 6.669522087344078e-05 | 6.95% | 7.47% | 1.07x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8765616641565867e-05 | 1.7594468190719536e-05 | 6.24% | 6.66% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.372200580823981e-05 | 1.7436121077634244e-05 | 26.50% | 36.05% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7662514952921993e-05 | 1.951353542828663e-05 | 29.46% | 41.76% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.763766912987735e-05 | 1.6125100124780546e-05 | 8.58% | 9.38% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.793255926019265e-05 | 1.688798665168278e-05 | 5.83% | 6.19% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.859571711307587e-05 | 1.7530586043234777e-05 | 5.73% | 6.08% | 1.06x | ✅ |
| `humanize_seconds[zero]` | 8.937532174845176e-07 | 6.885445612789955e-07 | 22.96% | 29.80% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.7244786766122102e-05 | 2.6427921608838865e-05 | 3.00% | 3.09% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.6970020286107125e-05 | 2.6211882095666296e-05 | 2.81% | 2.89% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.6754856480928096e-05 | 2.5801665791637004e-05 | 3.56% | 3.69% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.885120522477999e-06 | 4.360423151992625e-06 | 10.74% | 12.03% | 1.12x | ✅ |
| `is_ipfs_uri[empty]` | 1.811498562579653e-05 | 1.851237142196798e-05 | -2.19% | -2.15% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.216558311024367e-05 | 3.244588496806784e-05 | -0.87% | -0.86% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.037704346297844e-05 | 3.079021180378243e-05 | -1.36% | -1.34% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.382618495355522e-05 | 3.299154239054173e-05 | 2.47% | 2.53% | 1.03x | ✅ |
