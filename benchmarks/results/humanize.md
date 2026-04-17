#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.52659737728908e-06 | 2.7269032503215843e-06 | 39.76% | 66.00% | 1.66x | ✅ |
| `humanize_bytes[empty]` | 1.205638824381753e-06 | 9.123980162096601e-07 | 24.32% | 32.14% | 1.32x | ✅ |
| `humanize_bytes[long]` | 4.301264762532192e-06 | 2.617051916475071e-06 | 39.16% | 64.36% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.6276092643294088e-06 | 1.318976326152318e-06 | 18.96% | 23.40% | 1.23x | ✅ |
| `humanize_hash[32-bytes]` | 4.799179229358396e-06 | 2.78336186227393e-06 | 42.00% | 72.42% | 1.72x | ✅ |
| `humanize_hash[empty]` | 1.4102202216946115e-06 | 8.780063853605745e-07 | 37.74% | 60.62% | 1.61x | ✅ |
| `humanize_hash[long]` | 4.496515980527207e-06 | 2.4521808054045024e-06 | 45.46% | 83.37% | 1.83x | ✅ |
| `humanize_hash[short]` | 1.7528817888508103e-06 | 1.2979084850331737e-06 | 25.96% | 35.05% | 1.35x | ✅ |
| `humanize_hexstr[empty]` | 1.9890153701180357e-06 | 6.989691551056423e-07 | 64.86% | 184.56% | 2.85x | ✅ |
| `humanize_hexstr[short-0x]` | 4.999964771415921e-06 | 2.5947630839926e-06 | 48.10% | 92.69% | 1.93x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.117557366279114e-06 | 2.181863068159642e-06 | 47.01% | 88.72% | 1.89x | ✅ |
| `humanize_hexstr[very-long-0x]` | 5.030920697803495e-06 | 2.580247987148642e-06 | 48.71% | 94.98% | 1.95x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.210496770457015e-06 | 2.0961548614105666e-06 | 50.22% | 100.87% | 2.01x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.1355378178204444e-05 | 2.5420719464402223e-05 | 18.93% | 23.35% | 1.23x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.848267071713955e-05 | 3.075981916218321e-05 | 20.07% | 25.11% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.328053627245049e-07 | 6.179011392933468e-07 | 33.76% | 50.96% | 1.51x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.7488780110475746e-05 | 3.861840086328403e-05 | 18.68% | 22.97% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.740833205978696e-05 | 1.9831495069728126e-05 | 27.64% | 38.21% | 1.38x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.144441810171769e-05 | 3.45014474918887e-05 | 16.75% | 20.12% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.792006850004384e-05 | 6.917397719817027e-05 | -1.85% | -1.81% | 0.98x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9861949576120492e-05 | 1.7472513207780016e-05 | 12.03% | 13.68% | 1.14x | ✅ |
| `humanize_seconds[negative]` | 2.5098101246230152e-05 | 1.4419477315470462e-05 | 42.55% | 74.06% | 1.74x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.925359044965005e-05 | 1.7373801750571543e-05 | 40.61% | 68.38% | 1.68x | ✅ |
| `humanize_seconds[one-hour]` | 1.8674381222376754e-05 | 1.5711411196991952e-05 | 15.87% | 18.86% | 1.19x | ✅ |
| `humanize_seconds[one-minute]` | 1.891819591332353e-05 | 1.674040398607411e-05 | 11.51% | 13.01% | 1.13x | ✅ |
| `humanize_seconds[one-second]` | 2.0345920807118406e-05 | 1.7186117872809113e-05 | 15.53% | 18.39% | 1.18x | ✅ |
| `humanize_seconds[zero]` | 1.030599493499582e-06 | 8.691902896531561e-07 | 15.66% | 18.57% | 1.19x | ✅ |
| `humanize_wei[ether]` | 2.7956450956329995e-05 | 2.7033466606325023e-05 | 3.30% | 3.41% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.8076336666241662e-05 | 2.7760911094910398e-05 | 1.12% | 1.14% | 1.01x | ✅ |
| `humanize_wei[wei]` | 2.8583226470722337e-05 | 2.6311284357933877e-05 | 7.95% | 8.63% | 1.09x | ✅ |
| `humanize_wei[zero]` | 5.185585257249751e-06 | 3.563587983603704e-06 | 31.28% | 45.52% | 1.46x | ✅ |
| `is_ipfs_uri[empty]` | 1.905749106554624e-05 | 1.9265001099595342e-05 | -1.09% | -1.08% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.440917225213536e-05 | 3.430747377215199e-05 | 0.30% | 0.30% | 1.00x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.234129707475459e-05 | 3.319529457584795e-05 | -2.64% | -2.57% | 0.97x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.519129015721806e-05 | 3.4416404719292155e-05 | 2.20% | 2.25% | 1.02x | ✅ |
