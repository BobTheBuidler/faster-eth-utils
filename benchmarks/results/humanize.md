#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.17705072281283e-06 | 2.6870372732527714e-06 | 35.67% | 55.45% | 1.55x | ✅ |
| `humanize_bytes[empty]` | 1.1610612916489107e-06 | 8.166171871926205e-07 | 29.67% | 42.18% | 1.42x | ✅ |
| `humanize_bytes[long]` | 3.949806005828267e-06 | 2.5627947789491455e-06 | 35.12% | 54.12% | 1.54x | ✅ |
| `humanize_bytes[short]` | 1.4897872828069913e-06 | 1.1821252359713433e-06 | 20.65% | 26.03% | 1.26x | ✅ |
| `humanize_hash[32-bytes]` | 4.395207156037529e-06 | 2.7518357824336424e-06 | 37.39% | 59.72% | 1.60x | ✅ |
| `humanize_hash[empty]` | 1.386232735039023e-06 | 8.554932595395522e-07 | 38.29% | 62.04% | 1.62x | ✅ |
| `humanize_hash[long]` | 4.17302640027999e-06 | 2.5175171210583426e-06 | 39.67% | 65.76% | 1.66x | ✅ |
| `humanize_hash[short]` | 1.7156505504528464e-06 | 1.1881070800908512e-06 | 30.75% | 44.40% | 1.44x | ✅ |
| `humanize_hexstr[empty]` | 1.93897074676799e-06 | 6.801734483124016e-07 | 64.92% | 185.07% | 2.85x | ✅ |
| `humanize_hexstr[short-0x]` | 4.662056213586572e-06 | 2.6072858731494e-06 | 44.07% | 78.81% | 1.79x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9778103116346e-06 | 2.137218189411921e-06 | 46.27% | 86.12% | 1.86x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.711977857017417e-06 | 2.5938460805313373e-06 | 44.95% | 81.66% | 1.82x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.943845476878381e-06 | 2.1151504977422126e-06 | 46.37% | 86.46% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0271686255258547e-05 | 2.3496390602448206e-05 | 22.38% | 28.84% | 1.29x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.689915472675286e-05 | 2.817300962442011e-05 | 23.65% | 30.97% | 1.31x | ✅ |
| `humanize_integer_sequence[empty]` | 8.973132468827138e-07 | 5.706377148886969e-07 | 36.41% | 57.25% | 1.57x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5749862450068066e-05 | 3.5648740518462354e-05 | 22.08% | 28.34% | 1.28x | ✅ |
| `humanize_integer_sequence[single]` | 2.6669211146632515e-05 | 1.933962838747848e-05 | 27.48% | 37.90% | 1.38x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.040536436420947e-05 | 3.1613866406430185e-05 | 21.76% | 27.81% | 1.28x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.675874434458564e-05 | 6.544352927783215e-05 | 1.97% | 2.01% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8542321518601324e-05 | 1.548775573371126e-05 | 16.47% | 19.72% | 1.20x | ✅ |
| `humanize_seconds[negative]` | 2.239312171377013e-05 | 1.3011188434290232e-05 | 41.90% | 72.11% | 1.72x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.615467250465421e-05 | 1.5235777546141116e-05 | 41.75% | 71.67% | 1.72x | ✅ |
| `humanize_seconds[one-hour]` | 1.750803939790544e-05 | 1.4137734339991374e-05 | 19.25% | 23.84% | 1.24x | ✅ |
| `humanize_seconds[one-minute]` | 1.7642227570156558e-05 | 1.4795764150880486e-05 | 16.13% | 19.24% | 1.19x | ✅ |
| `humanize_seconds[one-second]` | 1.8634193095762238e-05 | 1.547481901237182e-05 | 16.95% | 20.42% | 1.20x | ✅ |
| `humanize_seconds[zero]` | 8.770083807604428e-07 | 6.931278156584109e-07 | 20.97% | 26.53% | 1.27x | ✅ |
| `humanize_wei[ether]` | 2.6774460032339243e-05 | 2.5453542820876188e-05 | 4.93% | 5.19% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.6725222183773965e-05 | 2.498065756960197e-05 | 6.53% | 6.98% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.6642072322823095e-05 | 2.5213333496127385e-05 | 5.36% | 5.67% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.834992590362699e-06 | 3.275637676058404e-06 | 32.25% | 47.60% | 1.48x | ✅ |
| `is_ipfs_uri[empty]` | 1.8181829714035905e-05 | 1.888103664835555e-05 | -3.85% | -3.70% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.24007622916809e-05 | 3.2176089359759235e-05 | 0.69% | 0.70% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.0044184703207575e-05 | 3.0554139612322285e-05 | -1.70% | -1.67% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.296823777311286e-05 | 3.240110920005606e-05 | 1.72% | 1.75% | 1.02x | ✅ |
