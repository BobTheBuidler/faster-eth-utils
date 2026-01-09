#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.214149487677847e-06 | 2.749892764484187e-06 | 34.75% | 53.25% | 1.53x | ✅ |
| `humanize_bytes[empty]` | 1.0840008351691295e-06 | 8.073448216027131e-07 | 25.52% | 34.27% | 1.34x | ✅ |
| `humanize_bytes[long]` | 3.975440819635068e-06 | 2.4242549227591948e-06 | 39.02% | 63.99% | 1.64x | ✅ |
| `humanize_bytes[short]` | 1.4436411927317341e-06 | 1.0825787257122906e-06 | 25.01% | 33.35% | 1.33x | ✅ |
| `humanize_hash[32-bytes]` | 4.549198509820864e-06 | 2.6733596107782068e-06 | 41.23% | 70.17% | 1.70x | ✅ |
| `humanize_hash[empty]` | 1.308819991799039e-06 | 8.374691606133705e-07 | 36.01% | 56.28% | 1.56x | ✅ |
| `humanize_hash[long]` | 4.268159377279379e-06 | 2.4465904364043155e-06 | 42.68% | 74.45% | 1.74x | ✅ |
| `humanize_hash[short]` | 1.6645627816162894e-06 | 1.0896761404292824e-06 | 34.54% | 52.76% | 1.53x | ✅ |
| `humanize_hexstr[empty]` | 1.8352353897435498e-06 | 6.263378937060862e-07 | 65.87% | 193.01% | 2.93x | ✅ |
| `humanize_hexstr[short-0x]` | 4.536721041700209e-06 | 2.482106028222601e-06 | 45.29% | 82.78% | 1.83x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.7562687504335435e-06 | 2.030927209259016e-06 | 45.93% | 84.95% | 1.85x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.55583416638599e-06 | 2.5196025379505897e-06 | 44.70% | 80.82% | 1.81x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.761002204216474e-06 | 2.024921467969505e-06 | 46.16% | 85.74% | 1.86x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.041859676013951e-05 | 2.4611531339814383e-05 | 19.09% | 23.59% | 1.24x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.677527535760233e-05 | 3.0295595338163425e-05 | 17.62% | 21.39% | 1.21x | ✅ |
| `humanize_integer_sequence[empty]` | 9.022318601572187e-07 | 5.643649060792587e-07 | 37.45% | 59.87% | 1.60x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.530774727288576e-05 | 3.826666261852272e-05 | 15.54% | 18.40% | 1.18x | ✅ |
| `humanize_integer_sequence[single]` | 2.6440042694782603e-05 | 2.024489564431639e-05 | 23.43% | 30.60% | 1.31x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.051148011622791e-05 | 3.38839605723696e-05 | 16.36% | 19.56% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.744143760420517e-05 | 6.702593609347993e-05 | 0.62% | 0.62% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.904919164131832e-05 | 1.796167825126638e-05 | 5.71% | 6.05% | 1.06x | ✅ |
| `humanize_seconds[negative]` | 2.35230658459001e-05 | 1.736304481468882e-05 | 26.19% | 35.48% | 1.35x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.74399355600177e-05 | 2.0875992006051508e-05 | 23.92% | 31.44% | 1.31x | ✅ |
| `humanize_seconds[one-hour]` | 1.8052405993142035e-05 | 1.6548663323687293e-05 | 8.33% | 9.09% | 1.09x | ✅ |
| `humanize_seconds[one-minute]` | 1.8381739234143563e-05 | 1.7262855848818385e-05 | 6.09% | 6.48% | 1.06x | ✅ |
| `humanize_seconds[one-second]` | 1.9090580336535736e-05 | 1.798130792040644e-05 | 5.81% | 6.17% | 1.06x | ✅ |
| `humanize_seconds[zero]` | 8.655163333757165e-07 | 6.602334037988109e-07 | 23.72% | 31.09% | 1.31x | ✅ |
| `humanize_wei[ether]` | 2.725501398906566e-05 | 2.6225479919195754e-05 | 3.78% | 3.93% | 1.04x | ✅ |
| `humanize_wei[gwei]` | 2.6926250546540684e-05 | 2.5937963942814698e-05 | 3.67% | 3.81% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.6598291153108328e-05 | 2.544896960258245e-05 | 4.32% | 4.52% | 1.05x | ✅ |
| `humanize_wei[zero]` | 4.753838674216438e-06 | 3.5899554106207966e-06 | 24.48% | 32.42% | 1.32x | ✅ |
| `is_ipfs_uri[empty]` | 1.866400245405124e-05 | 1.904778295724066e-05 | -2.06% | -2.01% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.2965805410860543e-05 | 3.2579089974642816e-05 | 1.17% | 1.19% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.067832126779076e-05 | 3.103875458413711e-05 | -1.17% | -1.16% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.340994371582886e-05 | 3.3411586217745444e-05 | -0.00% | -0.00% | 1.00x | ❌ |
