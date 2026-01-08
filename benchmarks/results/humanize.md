#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.249550855892694e-06 | 2.8516096874171985e-06 | 32.90% | 49.02% | 1.49x | ✅ |
| `humanize_bytes[empty]` | 1.0891066542792092e-06 | 8.09763451003319e-07 | 25.65% | 34.50% | 1.34x | ✅ |
| `humanize_bytes[long]` | 4.0445186464162016e-06 | 2.6716377169308324e-06 | 33.94% | 51.39% | 1.51x | ✅ |
| `humanize_bytes[short]` | 1.4470841165154247e-06 | 1.1146785352942542e-06 | 22.97% | 29.82% | 1.30x | ✅ |
| `humanize_hash[32-bytes]` | 4.478470360072531e-06 | 2.859043164931016e-06 | 36.16% | 56.64% | 1.57x | ✅ |
| `humanize_hash[empty]` | 1.341972071136475e-06 | 8.659816125476064e-07 | 35.47% | 54.97% | 1.55x | ✅ |
| `humanize_hash[long]` | 4.303250583986074e-06 | 2.6572858332683965e-06 | 38.25% | 61.94% | 1.62x | ✅ |
| `humanize_hash[short]` | 1.6611060010932206e-06 | 1.1752262581778733e-06 | 29.25% | 41.34% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.8441616901164033e-06 | 6.27767060213708e-07 | 65.96% | 193.77% | 2.94x | ✅ |
| `humanize_hexstr[short-0x]` | 4.518719631417061e-06 | 2.5445730127612007e-06 | 43.69% | 77.58% | 1.78x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.775397232990531e-06 | 2.1389818580807047e-06 | 43.34% | 76.50% | 1.77x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.572962362530466e-06 | 2.549733564666721e-06 | 44.24% | 79.35% | 1.79x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.8101368792573187e-06 | 2.063566400616738e-06 | 45.84% | 84.64% | 1.85x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.0400699628125758e-05 | 2.4369871853388177e-05 | 19.84% | 24.75% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.675805466896441e-05 | 2.922297431257764e-05 | 20.50% | 25.78% | 1.26x | ✅ |
| `humanize_integer_sequence[empty]` | 9.33922713091632e-07 | 6.098897670083174e-07 | 34.70% | 53.13% | 1.53x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.547282984083408e-05 | 3.684903056823016e-05 | 18.96% | 23.40% | 1.23x | ✅ |
| `humanize_integer_sequence[single]` | 2.7027783390689735e-05 | 2.0060860484408046e-05 | 25.78% | 34.73% | 1.35x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.106613706353703e-05 | 3.263901162845814e-05 | 20.52% | 25.82% | 1.26x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.907223100794077e-05 | 6.776524739322068e-05 | 1.89% | 1.93% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9094331702954153e-05 | 1.7838082449864343e-05 | 6.58% | 7.04% | 1.07x | ✅ |
| `humanize_seconds[negative]` | 2.4066762400386837e-05 | 1.7532198834759202e-05 | 27.15% | 37.27% | 1.37x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.759052740997062e-05 | 1.955153484782063e-05 | 29.14% | 41.12% | 1.41x | ✅ |
| `humanize_seconds[one-hour]` | 1.8103813158265324e-05 | 1.651169230969062e-05 | 8.79% | 9.64% | 1.10x | ✅ |
| `humanize_seconds[one-minute]` | 1.8259133931584135e-05 | 1.728923254511154e-05 | 5.31% | 5.61% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.8995518907528658e-05 | 1.7995010017200976e-05 | 5.27% | 5.56% | 1.06x | ✅ |
| `humanize_seconds[zero]` | 8.656842218113029e-07 | 6.466114750363098e-07 | 25.31% | 33.88% | 1.34x | ✅ |
| `humanize_wei[ether]` | 2.7624524728562957e-05 | 2.70749422959856e-05 | 1.99% | 2.03% | 1.02x | ✅ |
| `humanize_wei[gwei]` | 2.7413720296777e-05 | 2.6933944500785933e-05 | 1.75% | 1.78% | 1.02x | ✅ |
| `humanize_wei[wei]` | 2.7189278792409572e-05 | 2.635786812405151e-05 | 3.06% | 3.15% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.820878152151514e-06 | 4.095376195252171e-06 | 15.05% | 17.72% | 1.18x | ✅ |
| `is_ipfs_uri[empty]` | 1.8482514246757143e-05 | 1.9200757321022143e-05 | -3.89% | -3.74% | 0.96x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.384310339697747e-05 | 3.3494775887548906e-05 | 1.03% | 1.04% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.1069644730698446e-05 | 3.153641031312168e-05 | -1.50% | -1.48% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.408953066736671e-05 | 3.399583797293575e-05 | 0.27% | 0.28% | 1.00x | ✅ |
