#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.248461944941836e-06 | 2.715872804856488e-06 | 36.07% | 56.43% | 1.56x | ✅ |
| `humanize_bytes[empty]` | 1.1299523601824278e-06 | 8.155077376447103e-07 | 27.83% | 38.56% | 1.39x | ✅ |
| `humanize_bytes[long]` | 4.020522389834087e-06 | 2.4983704147021362e-06 | 37.86% | 60.93% | 1.61x | ✅ |
| `humanize_bytes[short]` | 1.5203249394556055e-06 | 1.0997481858710783e-06 | 27.66% | 38.24% | 1.38x | ✅ |
| `humanize_hash[32-bytes]` | 4.501947748161672e-06 | 2.7338497506771277e-06 | 39.27% | 64.67% | 1.65x | ✅ |
| `humanize_hash[empty]` | 1.3561802201229081e-06 | 8.335437459444288e-07 | 38.54% | 62.70% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.2935896740904355e-06 | 2.5197158055734293e-06 | 41.31% | 70.40% | 1.70x | ✅ |
| `humanize_hash[short]` | 1.7314669220794146e-06 | 1.1300490073714038e-06 | 34.73% | 53.22% | 1.53x | ✅ |
| `humanize_hexstr[empty]` | 1.9008293409236418e-06 | 6.294896557901902e-07 | 66.88% | 201.96% | 3.02x | ✅ |
| `humanize_hexstr[short-0x]` | 4.5291545936229865e-06 | 2.41693554614316e-06 | 46.64% | 87.39% | 1.87x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.8038382247575097e-06 | 2.000533797796382e-06 | 47.41% | 90.14% | 1.90x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.599727335704783e-06 | 2.4966120765256404e-06 | 45.72% | 84.24% | 1.84x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8001086557378034e-06 | 2.013361075268271e-06 | 47.02% | 88.74% | 1.89x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.041934074264825e-05 | 2.4374845475132566e-05 | 19.87% | 24.80% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.6659586764639835e-05 | 2.9935984741727977e-05 | 18.34% | 22.46% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 8.988820420135889e-07 | 5.787779470872367e-07 | 35.61% | 55.31% | 1.55x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.571704679254172e-05 | 3.7603135536293566e-05 | 17.75% | 21.58% | 1.22x | ✅ |
| `humanize_integer_sequence[single]` | 2.651618190841449e-05 | 2.0134976435958372e-05 | 24.07% | 31.69% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.065530637224114e-05 | 3.345380605401566e-05 | 17.71% | 21.53% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.768189740871874e-05 | 6.66618073705722e-05 | 1.51% | 1.53% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9198958637066004e-05 | 1.839468262082404e-05 | 4.19% | 4.37% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.3700358521903954e-05 | 1.783142827821315e-05 | 24.76% | 32.91% | 1.33x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7748757926381842e-05 | 2.028617987470859e-05 | 26.89% | 36.79% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.809548305508838e-05 | 1.6760903992148972e-05 | 7.38% | 7.96% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8523122636275713e-05 | 1.7631984241198225e-05 | 4.81% | 5.05% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.9264848519853566e-05 | 1.8328209517750895e-05 | 4.86% | 5.11% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.950149075043408e-07 | 7.611954504261857e-07 | 14.95% | 17.58% | 1.18x | ✅ |
| `humanize_wei[ether]` | 2.738728593024551e-05 | 2.6277768114851217e-05 | 4.05% | 4.22% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.7106023962737743e-05 | 2.5938363594175453e-05 | 4.31% | 4.50% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.7070221003490194e-05 | 2.550223052759069e-05 | 5.79% | 6.15% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.813591712287231e-06 | 3.713893525278698e-06 | 22.85% | 29.61% | 1.30x | ✅ |
| `is_ipfs_uri[empty]` | 1.8409792530463574e-05 | 1.8980486689971267e-05 | -3.10% | -3.01% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.34488018108328e-05 | 3.29623347868486e-05 | 1.45% | 1.48% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.071904133616684e-05 | 3.1051711587149466e-05 | -1.08% | -1.07% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.367945322754992e-05 | 3.308972858619727e-05 | 1.75% | 1.78% | 1.02x | ✅ |
