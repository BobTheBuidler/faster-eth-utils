#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.238900541045549e-06 | 2.842201971222647e-06 | 32.95% | 49.14% | 1.49x | ✅ |
| `humanize_bytes[empty]` | 1.1383492582833128e-06 | 9.817657764929298e-07 | 13.76% | 15.95% | 1.16x | ✅ |
| `humanize_bytes[long]` | 4.004004504441992e-06 | 2.6609123338309126e-06 | 33.54% | 50.47% | 1.50x | ✅ |
| `humanize_bytes[short]` | 1.5149333228970207e-06 | 1.2132290163047473e-06 | 19.92% | 24.87% | 1.25x | ✅ |
| `humanize_hash[32-bytes]` | 4.427563836737863e-06 | 2.835571421090124e-06 | 35.96% | 56.14% | 1.56x | ✅ |
| `humanize_hash[empty]` | 1.3532149237686966e-06 | 9.0922518521545e-07 | 32.81% | 48.83% | 1.49x | ✅ |
| `humanize_hash[long]` | 4.275373946384787e-06 | 2.6407971910291247e-06 | 38.23% | 61.90% | 1.62x | ✅ |
| `humanize_hash[short]` | 1.704811833269414e-06 | 1.2895501092902726e-06 | 24.36% | 32.20% | 1.32x | ✅ |
| `humanize_hexstr[empty]` | 1.8695935504716944e-06 | 6.377454590029518e-07 | 65.89% | 193.16% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.564538505335913e-06 | 2.394641410459619e-06 | 47.54% | 90.61% | 1.91x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.8056288921418007e-06 | 2.0308903601626817e-06 | 46.63% | 87.39% | 1.87x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.598721677639377e-06 | 2.5062360817024776e-06 | 45.50% | 83.49% | 1.83x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8012950257152846e-06 | 2.018751858997006e-06 | 46.89% | 88.30% | 1.88x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0520165921493036e-05 | 2.493078401824634e-05 | 18.31% | 22.42% | 1.22x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.71098963805578e-05 | 2.919588148998493e-05 | 21.33% | 27.11% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.277613104672828e-07 | 5.803611541268354e-07 | 37.44% | 59.86% | 1.60x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5525172436896015e-05 | 3.684053333967884e-05 | 19.08% | 23.57% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.6274543566659056e-05 | 2.0126180267884353e-05 | 23.40% | 30.55% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.095168482798159e-05 | 3.239347318487506e-05 | 20.90% | 26.42% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.70225796466459e-05 | 6.585101901938908e-05 | 1.75% | 1.78% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.8821247224603902e-05 | 1.8024913944790046e-05 | 4.23% | 4.42% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.376119918386511e-05 | 1.7710679590205387e-05 | 25.46% | 34.16% | 1.34x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.805641763368001e-05 | 1.977653550373404e-05 | 29.51% | 41.87% | 1.42x | ✅ |
| `humanize_seconds[one-hour]` | 1.7944888244338057e-05 | 1.6490925328103708e-05 | 8.10% | 8.82% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.812867817934234e-05 | 1.7271659418462022e-05 | 4.73% | 4.96% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.907720952768289e-05 | 1.778913835376692e-05 | 6.75% | 7.24% | 1.07x | ✅ |
| `humanize_seconds[zero]` | 8.983208331214238e-07 | 6.761048898192039e-07 | 24.74% | 32.87% | 1.33x | ✅ |
| `humanize_wei[ether]` | 2.791440722085385e-05 | 2.7364953525060543e-05 | 1.97% | 2.01% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.6914156508379783e-05 | 2.7352422971655752e-05 | -1.63% | -1.60% | 0.98x | ❌ |
| `humanize_wei[wei]` | 2.7360766468269308e-05 | 2.6678580382035757e-05 | 2.49% | 2.56% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.783966012301347e-06 | 4.1063014730310104e-06 | 14.17% | 16.50% | 1.17x | ✅ |
| `is_ipfs_uri[empty]` | 1.8537029839138205e-05 | 1.882903246963286e-05 | -1.58% | -1.55% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.289037647685056e-05 | 3.261899692379393e-05 | 0.83% | 0.83% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.068298876646037e-05 | 3.110515710037405e-05 | -1.38% | -1.36% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3692808139565936e-05 | 3.3057266865052265e-05 | 1.89% | 1.92% | 1.02x | ✅ |
