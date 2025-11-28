#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.20649197421377e-06 | 2.5303732713255957e-06 | 39.85% | 66.24% | 1.66x | ✅ |
| `humanize_bytes[empty]` | 1.168099950346128e-06 | 8.631988535176831e-07 | 26.10% | 35.32% | 1.35x | ✅ |
| `humanize_bytes[long]` | 3.9916167015097905e-06 | 2.3405955176561213e-06 | 41.36% | 70.54% | 1.71x | ✅ |
| `humanize_bytes[short]` | 1.4756053150124158e-06 | 1.1495578818010117e-06 | 22.10% | 28.36% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.427428583796383e-06 | 2.5263123304072724e-06 | 42.94% | 75.25% | 1.75x | ✅ |
| `humanize_hash[empty]` | 1.428923012340307e-06 | 8.766448792798026e-07 | 38.65% | 63.00% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.183443952163549e-06 | 2.359667279668081e-06 | 43.60% | 77.29% | 1.77x | ✅ |
| `humanize_hash[short]` | 1.62927756445849e-06 | 1.137119611388899e-06 | 30.21% | 43.28% | 1.43x | ✅ |
| `humanize_hexstr[empty]` | 1.8630669504275697e-06 | 6.648966211050036e-07 | 64.31% | 180.20% | 2.80x | ✅ |
| `humanize_hexstr[short-0x]` | 4.645104698756456e-06 | 2.4228000508062317e-06 | 47.84% | 91.72% | 1.92x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.94190849256279e-06 | 1.9340479774610793e-06 | 50.94% | 103.82% | 2.04x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.767551665358406e-06 | 2.3712414357564516e-06 | 50.26% | 101.06% | 2.01x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.9493901992802006e-06 | 1.9389195691781437e-06 | 50.91% | 103.69% | 2.04x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.051476609742229e-05 | 2.3802954610084364e-05 | 22.00% | 28.20% | 1.28x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.658804767569795e-05 | 2.884203270037331e-05 | 21.17% | 26.86% | 1.27x | ✅ |
| `humanize_integer_sequence[empty]` | 9.448165521345342e-07 | 5.768087837878067e-07 | 38.95% | 63.80% | 1.64x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.4807576638922585e-05 | 3.6295569211764946e-05 | 19.00% | 23.45% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.723527979379113e-05 | 1.9612059268368094e-05 | 27.99% | 38.87% | 1.39x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0150546111598285e-05 | 3.2127352829203224e-05 | 19.98% | 24.97% | 1.25x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.808528839788315e-05 | 6.7067652813641e-05 | 1.49% | 1.52% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.887075684390608e-05 | 1.7301701307763916e-05 | 8.31% | 9.07% | 1.09x | ✅ |
| `humanize_seconds[negative]` | 2.392394538913843e-05 | 1.7088312984865255e-05 | 28.57% | 40.00% | 1.40x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7832261831068864e-05 | 1.9495938431549373e-05 | 29.95% | 42.76% | 1.43x | ✅ |
| `humanize_seconds[one-hour]` | 1.768537576735292e-05 | 1.6120608299414456e-05 | 8.85% | 9.71% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.7856878428337573e-05 | 1.6812690716524068e-05 | 5.85% | 6.21% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.8822552378939844e-05 | 1.7236223588891846e-05 | 8.43% | 9.20% | 1.09x | ✅ |
| `humanize_seconds[zero]` | 8.96242743983554e-07 | 6.70765460180577e-07 | 25.16% | 33.61% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.7485595695521805e-05 | 2.7064891496450738e-05 | 1.53% | 1.55% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.7131562636993485e-05 | 2.6823995759237785e-05 | 1.13% | 1.15% | 1.01x | ✅ |
| `humanize_wei[wei]` | 2.7040349678999988e-05 | 2.6104897053214387e-05 | 3.46% | 3.58% | 1.04x | ✅ |
| `humanize_wei[zero]` | 4.940114751011025e-06 | 4.359164976397129e-06 | 11.76% | 13.33% | 1.13x | ✅ |
| `is_ipfs_uri[empty]` | 1.8166024357999116e-05 | 1.858713308120555e-05 | -2.32% | -2.27% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.320560356529264e-05 | 3.323108914750074e-05 | -0.08% | -0.08% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.0899863663754354e-05 | 3.171446524288032e-05 | -2.64% | -2.57% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.419694209156793e-05 | 3.366781941994487e-05 | 1.55% | 1.57% | 1.02x | ✅ |
