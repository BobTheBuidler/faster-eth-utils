#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.307222208304319e-06 | 2.741360857101767e-06 | 36.35% | 57.12% | 1.57x | ✅ |
| `humanize_bytes[empty]` | 1.0961409662783201e-06 | 8.020910182143802e-07 | 26.83% | 36.66% | 1.37x | ✅ |
| `humanize_bytes[long]` | 4.061406101015981e-06 | 2.4152850267376785e-06 | 40.53% | 68.15% | 1.68x | ✅ |
| `humanize_bytes[short]` | 1.4671912378795253e-06 | 1.0782590222962753e-06 | 26.51% | 36.07% | 1.36x | ✅ |
| `humanize_hash[32-bytes]` | 4.551168874132073e-06 | 2.7235290336138075e-06 | 40.16% | 67.11% | 1.67x | ✅ |
| `humanize_hash[empty]` | 1.334581402808671e-06 | 8.201898465055931e-07 | 38.54% | 62.72% | 1.63x | ✅ |
| `humanize_hash[long]` | 4.302221171158049e-06 | 2.439734932864878e-06 | 43.29% | 76.34% | 1.76x | ✅ |
| `humanize_hash[short]` | 1.6947533708149667e-06 | 1.2017238177264552e-06 | 29.09% | 41.03% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.8990618177599466e-06 | 6.328040660946592e-07 | 66.68% | 200.10% | 3.00x | ✅ |
| `humanize_hexstr[short-0x]` | 4.571098092012878e-06 | 2.458181571146731e-06 | 46.22% | 85.95% | 1.86x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.848704777439187e-06 | 2.1221826298830884e-06 | 44.86% | 81.36% | 1.81x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.6313500447463214e-06 | 2.5240288727781594e-06 | 45.50% | 83.49% | 1.83x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.7902297992166367e-06 | 2.0296395386101637e-06 | 46.45% | 86.74% | 1.87x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0271683802335127e-05 | 2.447580470205795e-05 | 19.15% | 23.68% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.641762732430249e-05 | 2.9816715434280643e-05 | 18.13% | 22.14% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 9.111332804207591e-07 | 5.903918515993267e-07 | 35.20% | 54.33% | 1.54x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5432185674552605e-05 | 3.7849728660234055e-05 | 16.69% | 20.03% | 1.20x | ✅ |
| `humanize_integer_sequence[single]` | 2.6392789615369052e-05 | 2.0278114632972e-05 | 23.17% | 30.15% | 1.30x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.001813314631991e-05 | 3.3256835822062354e-05 | 16.90% | 20.33% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.78643814131535e-05 | 6.650739474136667e-05 | 2.00% | 2.04% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9071361378401837e-05 | 1.836368793715943e-05 | 3.71% | 3.85% | 1.04x | ✅ |
| `humanize_seconds[negative]` | 2.391711935286993e-05 | 1.7812649838032192e-05 | 25.52% | 34.27% | 1.34x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7554922612049097e-05 | 2.009486116734142e-05 | 27.07% | 37.12% | 1.37x | ✅ |
| `humanize_seconds[one-hour]` | 1.8058684850419507e-05 | 1.6721684601068676e-05 | 7.40% | 8.00% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8373709504153107e-05 | 1.7538280543278614e-05 | 4.55% | 4.76% | 1.05x | ✅ |
| `humanize_seconds[one-second]` | 1.9137486333925988e-05 | 1.8211036331535364e-05 | 4.84% | 5.09% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.849741465047898e-07 | 6.815292697041649e-07 | 22.99% | 29.85% | 1.30x | ✅ |
| `humanize_wei[ether]` | 2.727696609989795e-05 | 2.6470799673682946e-05 | 2.96% | 3.05% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.693832242281015e-05 | 2.5885597323093264e-05 | 3.91% | 4.07% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.668075856401404e-05 | 2.540785902647076e-05 | 4.77% | 5.01% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.744043659172145e-06 | 3.6209298098361252e-06 | 23.67% | 31.02% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.847987312343391e-05 | 1.8995070033397532e-05 | -2.79% | -2.71% | 0.97x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.3145735701773416e-05 | 3.296333786992914e-05 | 0.55% | 0.55% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.086339990297773e-05 | 3.124933046622062e-05 | -1.25% | -1.24% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3665490605240214e-05 | 3.304901971697614e-05 | 1.83% | 1.87% | 1.02x | ✅ |
