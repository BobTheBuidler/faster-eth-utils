#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.53777140914408e-06 | 2.856943091875801e-06 | 37.04% | 58.83% | 1.59x | ✅ |
| `humanize_bytes[empty]` | 1.1349228014373076e-06 | 8.702425664533141e-07 | 23.32% | 30.41% | 1.30x | ✅ |
| `humanize_bytes[long]` | 4.254763411195546e-06 | 2.5927095764491902e-06 | 39.06% | 64.10% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.516398993109696e-06 | 1.1104271398522133e-06 | 26.77% | 36.56% | 1.37x | ✅ |
| `humanize_hash[32-bytes]` | 4.759839837447187e-06 | 2.7198079173866058e-06 | 42.86% | 75.01% | 1.75x | ✅ |
| `humanize_hash[empty]` | 1.3434489223145166e-06 | 9.256217543004012e-07 | 31.10% | 45.14% | 1.45x | ✅ |
| `humanize_hash[long]` | 4.49662723254527e-06 | 2.516058983465267e-06 | 44.05% | 78.72% | 1.79x | ✅ |
| `humanize_hash[short]` | 1.7592926248526064e-06 | 1.1662108430647277e-06 | 33.71% | 50.86% | 1.51x | ✅ |
| `humanize_hexstr[empty]` | 1.9065920176299302e-06 | 6.709469949776945e-07 | 64.81% | 184.16% | 2.84x | ✅ |
| `humanize_hexstr[short-0x]` | 4.854969352862746e-06 | 2.559598882290241e-06 | 47.28% | 89.68% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.0777603827032015e-06 | 2.0198164065317416e-06 | 50.47% | 101.89% | 2.02x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.82445276908248e-06 | 2.5211269892862402e-06 | 47.74% | 91.36% | 1.91x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.132991167638309e-06 | 2.0547738885153217e-06 | 50.28% | 101.14% | 2.01x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.126950244983716e-05 | 2.4727991163342436e-05 | 20.92% | 26.45% | 1.26x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.78198003365925e-05 | 3.0142990850811943e-05 | 20.30% | 25.47% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 8.663536299515708e-07 | 5.892806421050484e-07 | 31.98% | 47.02% | 1.47x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.656504171008255e-05 | 3.7727501949385004e-05 | 18.98% | 23.42% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.7299701378478327e-05 | 2.125786366861244e-05 | 22.13% | 28.42% | 1.28x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1468982787140694e-05 | 3.353561547275086e-05 | 19.13% | 23.66% | 1.24x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.998559131282367e-05 | 6.87949457018439e-05 | 1.70% | 1.73% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.952106611856276e-05 | 1.6900405252298178e-05 | 13.42% | 15.51% | 1.16x | ✅ |
| `humanize_seconds[negative]` | 2.4097480836550104e-05 | 1.446262586549629e-05 | 39.98% | 66.62% | 1.67x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.8309819253173537e-05 | 1.659643247736724e-05 | 41.38% | 70.58% | 1.71x | ✅ |
| `humanize_seconds[one-hour]` | 1.8812758737905575e-05 | 1.5713799899530805e-05 | 16.47% | 19.72% | 1.20x | ✅ |
| `humanize_seconds[one-minute]` | 1.8846769121249415e-05 | 1.631337201746242e-05 | 13.44% | 15.53% | 1.16x | ✅ |
| `humanize_seconds[one-second]` | 1.958575578398941e-05 | 1.6960903742688334e-05 | 13.40% | 15.48% | 1.15x | ✅ |
| `humanize_seconds[zero]` | 8.289126553847839e-07 | 6.90280058221577e-07 | 16.72% | 20.08% | 1.20x | ✅ |
| `humanize_wei[ether]` | 2.8906438290789395e-05 | 2.7252985029710023e-05 | 5.72% | 6.07% | 1.06x | ✅ |
| `humanize_wei[gwei]` | 2.8494556477972513e-05 | 2.6520691041418035e-05 | 6.93% | 7.44% | 1.07x | ✅ |
| `humanize_wei[wei]` | 2.8265101490080403e-05 | 2.608806007629512e-05 | 7.70% | 8.34% | 1.08x | ✅ |
| `humanize_wei[zero]` | 5.185749739527487e-06 | 3.1701994493739512e-06 | 38.87% | 63.58% | 1.64x | ✅ |
| `is_ipfs_uri[empty]` | 1.882707933481699e-05 | 1.9708020380286887e-05 | -4.68% | -4.47% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.404698845183504e-05 | 3.4282074145158615e-05 | -0.69% | -0.69% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.1883694329253305e-05 | 3.2652577934405165e-05 | -2.41% | -2.35% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4384909785272e-05 | 3.4719084401522234e-05 | -0.97% | -0.96% | 0.99x | ❌ |
