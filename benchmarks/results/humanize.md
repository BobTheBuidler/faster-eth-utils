#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.1453837342304775e-06 | 2.4064838424221115e-06 | 41.95% | 72.26% | 1.72x | ✅ |
| `humanize_bytes[empty]` | 1.1529467025506582e-06 | 8.699419110636405e-07 | 24.55% | 32.53% | 1.33x | ✅ |
| `humanize_bytes[long]` | 3.990866104863681e-06 | 2.2374915625580997e-06 | 43.93% | 78.36% | 1.78x | ✅ |
| `humanize_bytes[short]` | 1.4160392111331175e-06 | 1.0443751923690157e-06 | 26.25% | 35.59% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.488133389675197e-06 | 2.3977292202350335e-06 | 46.58% | 87.18% | 1.87x | ✅ |
| `humanize_hash[empty]` | 1.415060420640781e-06 | 8.583951244260975e-07 | 39.34% | 64.85% | 1.65x | ✅ |
| `humanize_hash[long]` | 4.3462166141701786e-06 | 2.21391570068889e-06 | 49.06% | 96.31% | 1.96x | ✅ |
| `humanize_hash[short]` | 1.6910709355991205e-06 | 1.0679571522712805e-06 | 36.85% | 58.35% | 1.58x | ✅ |
| `humanize_hexstr[empty]` | 2.009499179784737e-06 | 6.850958321208868e-07 | 65.91% | 193.32% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.77812604727451e-06 | 2.1851494698310277e-06 | 54.27% | 118.66% | 2.19x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.9342084375561885e-06 | 1.8408770785934098e-06 | 53.21% | 113.71% | 2.14x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.796431442596993e-06 | 2.1845492555881725e-06 | 54.45% | 119.56% | 2.20x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.072077182211246e-06 | 1.876588009752912e-06 | 53.92% | 116.99% | 2.17x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.13941589920783e-05 | 2.5010865224656006e-05 | 20.33% | 25.52% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.695248514544041e-05 | 3.044900169411588e-05 | 17.60% | 21.36% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 8.561493270602971e-07 | 6.458225185342578e-07 | 24.57% | 32.57% | 1.33x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.590229074391639e-05 | 3.725107255031328e-05 | 18.85% | 23.22% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.7763765801314308e-05 | 2.1561751181754273e-05 | 22.34% | 28.76% | 1.29x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.081446193170075e-05 | 3.352810296332581e-05 | 17.85% | 21.73% | 1.22x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 3.507734671878722e-05 | 3.2547900239110076e-05 | 7.21% | 7.77% | 1.08x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 2.0628877738435634e-05 | 1.8628812074454335e-05 | 9.70% | 10.74% | 1.11x | ✅ |
| `humanize_seconds[negative]` | 2.7542592903185666e-05 | 1.829066408134694e-05 | 33.59% | 50.58% | 1.51x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 3.227560879136071e-05 | 2.030343175975154e-05 | 37.09% | 58.97% | 1.59x | ✅ |
| `humanize_seconds[one-hour]` | 1.9818365951972754e-05 | 1.7811517217825104e-05 | 10.13% | 11.27% | 1.11x | ✅ |
| `humanize_seconds[one-minute]` | 1.975876727245626e-05 | 1.793859003011195e-05 | 9.21% | 10.15% | 1.10x | ✅ |
| `humanize_seconds[one-second]` | 2.0542230171426065e-05 | 1.8516365133009003e-05 | 9.86% | 10.94% | 1.11x | ✅ |
| `humanize_seconds[zero]` | 1.3314367258167058e-06 | 1.0861514902146442e-06 | 18.42% | 22.58% | 1.23x | ✅ |
| `humanize_wei[ether]` | 2.6684874490840128e-05 | 2.5495759406822876e-05 | 4.46% | 4.66% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.619675314699926e-05 | 2.4979700228838318e-05 | 4.65% | 4.87% | 1.05x | ✅ |
| `humanize_wei[wei]` | 2.604000640217725e-05 | 2.4186877917718393e-05 | 7.12% | 7.66% | 1.08x | ✅ |
| `humanize_wei[zero]` | 4.8443496281957345e-06 | 3.7846650016575457e-06 | 21.87% | 28.00% | 1.28x | ✅ |
| `is_ipfs_uri[empty]` | 1.3861984864299688e-05 | 1.3903551664784037e-05 | -0.30% | -0.30% | 1.00x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 1.7190519197223015e-05 | 1.6307898990872794e-05 | 5.13% | 5.41% | 1.05x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 1.4540515402047384e-05 | 1.4490909401245416e-05 | 0.34% | 0.34% | 1.00x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 1.7483043605148706e-05 | 1.6493599628618154e-05 | 5.66% | 6.00% | 1.06x | ✅ |
