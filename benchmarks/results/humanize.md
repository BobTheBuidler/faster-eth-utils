#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 3.871280862958553e-06 | 2.49218192665369e-06 | 35.62% | 55.34% | 1.55x | ✅ |
| `humanize_bytes[empty]` | 1.097684293691674e-06 | 7.658093112634585e-07 | 30.23% | 43.34% | 1.43x | ✅ |
| `humanize_bytes[long]` | 3.7071359218081057e-06 | 2.326926522321445e-06 | 37.23% | 59.31% | 1.59x | ✅ |
| `humanize_bytes[short]` | 1.462616281079207e-06 | 9.907260461705274e-07 | 32.26% | 47.63% | 1.48x | ✅ |
| `humanize_hash[32-bytes]` | 4.142521875778339e-06 | 2.5019056126686835e-06 | 39.60% | 65.57% | 1.66x | ✅ |
| `humanize_hash[empty]` | 1.3508371593368553e-06 | 7.760858145192337e-07 | 42.55% | 74.06% | 1.74x | ✅ |
| `humanize_hash[long]` | 3.966881378017869e-06 | 2.343381783494669e-06 | 40.93% | 69.28% | 1.69x | ✅ |
| `humanize_hash[short]` | 1.713734991620362e-06 | 1.0069932045074862e-06 | 41.24% | 70.18% | 1.70x | ✅ |
| `humanize_hexstr[empty]` | 1.7303287821324755e-06 | 6.040316207289379e-07 | 65.09% | 186.46% | 2.86x | ✅ |
| `humanize_hexstr[short-0x]` | 4.384783240205275e-06 | 2.2304479372978786e-06 | 49.13% | 96.59% | 1.97x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7156285299633154e-06 | 1.7986785606026042e-06 | 51.59% | 106.58% | 2.07x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.4396099923513785e-06 | 2.2785936301784703e-06 | 48.68% | 94.84% | 1.95x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.6926960643247363e-06 | 1.8000280394005338e-06 | 51.25% | 105.15% | 2.05x | ✅ |
| `humanize_integer_sequence[consecutive]` | 2.9254011822057457e-05 | 2.1716272878191577e-05 | 25.77% | 34.71% | 1.35x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.466335092274547e-05 | 2.6285123080779618e-05 | 24.17% | 31.87% | 1.32x | ✅ |
| `humanize_integer_sequence[empty]` | 7.780444883440013e-07 | 5.492843188625636e-07 | 29.40% | 41.65% | 1.42x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.2947721400026976e-05 | 3.373736113007651e-05 | 21.45% | 27.30% | 1.27x | ✅ |
| `humanize_integer_sequence[single]` | 2.5783663187102027e-05 | 1.8326387044972095e-05 | 28.92% | 40.69% | 1.41x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 3.805217896091102e-05 | 3.0078941817698112e-05 | 20.95% | 26.51% | 1.27x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.231415462919076e-05 | 6.282011642927648e-05 | -0.81% | -0.81% | 0.99x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.828793963324853e-05 | 1.6265782127554922e-05 | 11.06% | 12.43% | 1.12x | ✅ |
| `humanize_seconds[negative]` | 2.2820637607070086e-05 | 1.5743374737310943e-05 | 31.01% | 44.95% | 1.45x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.705043950611527e-05 | 1.8514322247116828e-05 | 31.56% | 46.11% | 1.46x | ✅ |
| `humanize_seconds[one-hour]` | 1.725992127539126e-05 | 1.5350141382123016e-05 | 11.06% | 12.44% | 1.12x | ✅ |
| `humanize_seconds[one-minute]` | 1.7680673750179664e-05 | 1.589163425184076e-05 | 10.12% | 11.26% | 1.11x | ✅ |
| `humanize_seconds[one-second]` | 1.8310355830825755e-05 | 1.626778697017209e-05 | 11.16% | 12.56% | 1.13x | ✅ |
| `humanize_seconds[zero]` | 7.473667726618917e-07 | 5.83541372924571e-07 | 21.92% | 28.07% | 1.28x | ✅ |
| `humanize_wei[ether]` | 2.6856308237221505e-05 | 2.617556492053372e-05 | 2.53% | 2.60% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.787822296019809e-05 | 2.5840185061429797e-05 | 7.31% | 7.89% | 1.08x | ✅ |
| `humanize_wei[wei]` | 2.6306041631537273e-05 | 2.504752327215513e-05 | 4.78% | 5.02% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.662905448306681e-06 | 4.162785150738206e-06 | 10.73% | 12.01% | 1.12x | ✅ |
| `is_ipfs_uri[empty]` | 1.677207776570131e-05 | 1.7517271534246045e-05 | -4.44% | -4.25% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.0399104826767053e-05 | 3.1146560946974576e-05 | -2.46% | -2.40% | 0.98x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 2.835186806502939e-05 | 2.9103924418419114e-05 | -2.65% | -2.58% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.109702333996004e-05 | 3.147023593812261e-05 | -1.20% | -1.19% | 0.99x | ❌ |
