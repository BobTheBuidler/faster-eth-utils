#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-humanize_seconds-to-reduce-int-calls/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.196919329491664e-06 | 2.7870088124270003e-06 | 33.59% | 50.59% | 1.51x | ✅ |
| `humanize_bytes[empty]` | 1.1005865244734352e-06 | 8.073735303058748e-07 | 26.64% | 36.32% | 1.36x | ✅ |
| `humanize_bytes[long]` | 4.005769254455944e-06 | 2.633255982091407e-06 | 34.26% | 52.12% | 1.52x | ✅ |
| `humanize_bytes[short]` | 1.4499590433569556e-06 | 1.1438441404160003e-06 | 21.11% | 26.76% | 1.27x | ✅ |
| `humanize_hash[32-bytes]` | 4.380618874184412e-06 | 2.840968574485373e-06 | 35.15% | 54.19% | 1.54x | ✅ |
| `humanize_hash[empty]` | 1.3451951181763403e-06 | 8.456739818270083e-07 | 37.13% | 59.07% | 1.59x | ✅ |
| `humanize_hash[long]` | 4.2369854846032345e-06 | 2.655240741865176e-06 | 37.33% | 59.57% | 1.60x | ✅ |
| `humanize_hash[short]` | 1.6934914502975816e-06 | 1.1429598536227647e-06 | 32.51% | 48.17% | 1.48x | ✅ |
| `humanize_hexstr[empty]` | 1.84730567028104e-06 | 6.222144656054353e-07 | 66.32% | 196.89% | 2.97x | ✅ |
| `humanize_hexstr[short-0x]` | 4.537603895833335e-06 | 2.491634014693678e-06 | 45.09% | 82.11% | 1.82x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7718844645687617e-06 | 1.988080988039209e-06 | 47.29% | 89.72% | 1.90x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.872476453797768e-06 | 2.5243143319633332e-06 | 48.19% | 93.02% | 1.93x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8063163665941828e-06 | 2.049022988586186e-06 | 46.17% | 85.76% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.073859523944614e-05 | 2.4265952157249417e-05 | 21.06% | 26.67% | 1.27x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.739803182174676e-05 | 2.9710130284747914e-05 | 20.56% | 25.88% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 8.985790397501359e-07 | 5.915040148465651e-07 | 34.17% | 51.91% | 1.52x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.626819677861255e-05 | 3.726662799441673e-05 | 19.46% | 24.15% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.6661896874634673e-05 | 2.010783271692557e-05 | 24.58% | 32.59% | 1.33x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.073452310768243e-05 | 3.284627946432853e-05 | 19.37% | 24.02% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.821009915927626e-05 | 6.821332795756442e-05 | -0.00% | -0.00% | 1.00x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9033075574172522e-05 | 1.7680363713009417e-05 | 7.11% | 7.65% | 1.08x | ✅ |
| `humanize_seconds[negative]` | 2.352137823204425e-05 | 1.7754633259656765e-05 | 24.52% | 32.48% | 1.32x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7260131893132717e-05 | 1.9878829007440767e-05 | 27.08% | 37.13% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.7768343499047508e-05 | 1.6540151585262037e-05 | 6.91% | 7.43% | 1.07x | ✅ |
| `humanize_seconds[one-minute]` | 1.808092731336025e-05 | 1.7249382921419586e-05 | 4.60% | 4.82% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.8791953164307072e-05 | 1.7665068924661068e-05 | 6.00% | 6.38% | 1.06x | ✅ |
| `humanize_seconds[zero]` | 8.708112474605345e-07 | 6.676077185732279e-07 | 23.33% | 30.44% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.7352677828131655e-05 | 2.6110033608516834e-05 | 4.54% | 4.76% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.7062377806689717e-05 | 2.617110403499048e-05 | 3.29% | 3.41% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.6924906063328974e-05 | 2.531208110430852e-05 | 5.99% | 6.37% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.8508854143728675e-06 | 3.5834347426166483e-06 | 26.13% | 35.37% | 1.35x | ✅ |
| `is_ipfs_uri[empty]` | 1.8633576899512203e-05 | 1.9377822416576854e-05 | -3.99% | -3.84% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.323910584816618e-05 | 3.385518447459425e-05 | -1.85% | -1.82% | 0.98x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.1081088999019874e-05 | 3.2304592544780537e-05 | -3.94% | -3.79% | 0.96x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3790085796624376e-05 | 3.436226390290819e-05 | -1.69% | -1.67% | 0.98x | ❌ |
