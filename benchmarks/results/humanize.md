#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.059382592978503e-06 | 2.589734600220934e-06 | 36.20% | 56.75% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.0728202163445092e-06 | 9.0103567223864e-07 | 16.01% | 19.07% | 1.19x | ✅ |
| `humanize_bytes[long]` | 3.9185577879931355e-06 | 2.3186687818944194e-06 | 40.83% | 69.00% | 1.69x | ✅ |
| `humanize_bytes[short]` | 1.423105457117591e-06 | 1.1100201416760446e-06 | 22.00% | 28.21% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.269318836812114e-06 | 2.502067212818526e-06 | 41.39% | 70.63% | 1.71x | ✅ |
| `humanize_hash[empty]` | 1.2791428571242126e-06 | 8.182966744411475e-07 | 36.03% | 56.32% | 1.56x | ✅ |
| `humanize_hash[long]` | 4.024618948397026e-06 | 2.390421408603726e-06 | 40.61% | 68.36% | 1.68x | ✅ |
| `humanize_hash[short]` | 1.56273780409645e-06 | 1.072566860592886e-06 | 31.37% | 45.70% | 1.46x | ✅ |
| `humanize_hexstr[empty]` | 1.804108136577021e-06 | 6.24468252480985e-07 | 65.39% | 188.90% | 2.89x | ✅ |
| `humanize_hexstr[short-0x]` | 4.327133932476283e-06 | 2.3406106135883723e-06 | 45.91% | 84.87% | 1.85x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.5961131523147054e-06 | 1.957905311706041e-06 | 45.55% | 83.67% | 1.84x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.529382150412394e-06 | 2.385747342855717e-06 | 47.33% | 89.85% | 1.90x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.6272636258778e-06 | 1.976450768733321e-06 | 45.51% | 83.52% | 1.84x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9293035008384398e-05 | 2.3386463087825576e-05 | 20.16% | 25.26% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.5468019207763885e-05 | 2.9146077028081903e-05 | 17.82% | 21.69% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 8.848804008600357e-07 | 6.416671234067411e-07 | 27.49% | 37.90% | 1.38x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.3236108587218655e-05 | 3.548369980483043e-05 | 17.93% | 21.85% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.5030539202772725e-05 | 1.940373783389247e-05 | 22.48% | 29.00% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.7490044539986555e-05 | 3.191488191771522e-05 | 14.87% | 17.47% | 1.17x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.424083645570046e-05 | 6.240355094205748e-05 | 2.86% | 2.94% | 1.03x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9113388954518355e-05 | 1.842029534415287e-05 | 3.63% | 3.76% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.3650387779708703e-05 | 1.7454179782336817e-05 | 26.20% | 35.50% | 1.35x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.718772146853779e-05 | 1.996189287326001e-05 | 26.58% | 36.20% | 1.36x | ✅ |
| `humanize_seconds[one-hour]` | 1.7859923207146316e-05 | 1.6738092387050143e-05 | 6.28% | 6.70% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.8099187063614928e-05 | 1.7440050282542503e-05 | 3.64% | 3.78% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.904195851071768e-05 | 1.8479655813390197e-05 | 2.95% | 3.04% | 1.03x | ✅ |
| `humanize_seconds[zero]` | 8.777850874024819e-07 | 8.124005046136756e-07 | 7.45% | 8.05% | 1.08x | ✅ |
| `humanize_wei[ether]` | 2.5239663438295854e-05 | 2.5100041000096476e-05 | 0.55% | 0.56% | 1.01x | ✅ |
| `humanize_wei[gwei]` | 2.6427115411841487e-05 | 2.421624459714068e-05 | 8.37% | 9.13% | 1.09x | ✅ |
| `humanize_wei[wei]` | 2.5696710850243664e-05 | 2.3845759307613146e-05 | 7.20% | 7.76% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.48990446345182e-06 | 3.4414368601951772e-06 | 23.35% | 30.47% | 1.30x | ✅ |
| `is_ipfs_uri[empty]` | 1.732415431523337e-05 | 1.787340839855899e-05 | -3.17% | -3.07% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.182143476603803e-05 | 3.082622792204566e-05 | 3.13% | 3.23% | 1.03x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 2.90195799473585e-05 | 3.022706869868528e-05 | -4.16% | -3.99% | 0.96x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.194247701690657e-05 | 3.144270565682527e-05 | 1.56% | 1.59% | 1.02x | ✅ |
