#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.168416586090861e-06 | 2.552992670329471e-06 | 38.75% | 63.28% | 1.63x | ✅ |
| `humanize_bytes[empty]` | 1.1099682759627048e-06 | 8.879932546201213e-07 | 20.00% | 25.00% | 1.25x | ✅ |
| `humanize_bytes[long]` | 3.958492707397153e-06 | 2.3977295255938076e-06 | 39.43% | 65.09% | 1.65x | ✅ |
| `humanize_bytes[short]` | 1.4778475206538225e-06 | 1.2177644801044941e-06 | 17.60% | 21.36% | 1.21x | ✅ |
| `humanize_hash[32-bytes]` | 4.42056261261412e-06 | 2.5732118861483704e-06 | 41.79% | 71.79% | 1.72x | ✅ |
| `humanize_hash[empty]` | 1.3720078822518358e-06 | 8.853201117854412e-07 | 35.47% | 54.97% | 1.55x | ✅ |
| `humanize_hash[long]` | 4.244746326857965e-06 | 2.3472459973426473e-06 | 44.70% | 80.84% | 1.81x | ✅ |
| `humanize_hash[short]` | 1.7102862250771205e-06 | 1.2120390189591791e-06 | 29.13% | 41.11% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.9763414980747367e-06 | 6.669924029513244e-07 | 66.25% | 196.31% | 2.96x | ✅ |
| `humanize_hexstr[short-0x]` | 4.826523279009804e-06 | 2.4335380393254916e-06 | 49.58% | 98.33% | 1.98x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.927024649908506e-06 | 1.940727464676781e-06 | 50.58% | 102.35% | 2.02x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.801796768421655e-06 | 2.3666227193172137e-06 | 50.71% | 102.90% | 2.03x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.993352893725046e-06 | 1.939779275642635e-06 | 51.42% | 105.87% | 2.06x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.073637211065658e-05 | 2.3185971237924984e-05 | 24.57% | 32.56% | 1.33x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.7851810831520125e-05 | 2.894412845384351e-05 | 23.53% | 30.78% | 1.31x | ✅ |
| `humanize_integer_sequence[empty]` | 9.525373332219927e-07 | 6.024773474404318e-07 | 36.75% | 58.10% | 1.58x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5925296109767665e-05 | 3.5920815540328224e-05 | 21.78% | 27.85% | 1.28x | ✅ |
| `humanize_integer_sequence[single]` | 2.6802173907570878e-05 | 1.930721920644217e-05 | 27.96% | 38.82% | 1.39x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.0953872066854004e-05 | 3.19441138534285e-05 | 22.00% | 28.20% | 1.28x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.964613596326715e-05 | 6.946416846430316e-05 | 0.26% | 0.26% | 1.00x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9679373858948888e-05 | 1.5782267808673416e-05 | 19.80% | 24.69% | 1.25x | ✅ |
| `humanize_seconds[negative]` | 2.43276571439316e-05 | 1.2966512024005547e-05 | 46.70% | 87.62% | 1.88x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.858516945873668e-05 | 1.5295635297405037e-05 | 46.49% | 86.88% | 1.87x | ✅ |
| `humanize_seconds[one-hour]` | 1.8600458869576605e-05 | 1.446397767597471e-05 | 22.24% | 28.60% | 1.29x | ✅ |
| `humanize_seconds[one-minute]` | 1.933868843582815e-05 | 1.5189363244683637e-05 | 21.46% | 27.32% | 1.27x | ✅ |
| `humanize_seconds[one-second]` | 1.9697021377700514e-05 | 1.5802574581004685e-05 | 19.77% | 24.64% | 1.25x | ✅ |
| `humanize_seconds[zero]` | 8.652498626077586e-07 | 8.131014985306853e-07 | 6.03% | 6.41% | 1.06x | ✅ |
| `humanize_wei[ether]` | 2.8272524859385046e-05 | 2.6925534619523758e-05 | 4.76% | 5.00% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.798408727339337e-05 | 2.644897207485673e-05 | 5.49% | 5.80% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.7715308917551937e-05 | 2.6115506791430087e-05 | 5.77% | 6.13% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.83042171896623e-06 | 2.920778564421139e-06 | 39.53% | 65.38% | 1.65x | ✅ |
| `is_ipfs_uri[empty]` | 1.8523202794266065e-05 | 1.9402252987863655e-05 | -4.75% | -4.53% | 0.95x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.418735457633961e-05 | 3.423668050051813e-05 | -0.14% | -0.14% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.225761499314643e-05 | 3.2393310332253804e-05 | -0.42% | -0.42% | 1.00x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.494098449492261e-05 | 3.452829082269437e-05 | 1.18% | 1.20% | 1.01x | ✅ |
