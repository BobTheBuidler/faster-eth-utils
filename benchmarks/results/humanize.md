#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.445374054059459e-06 | 3.02823876257459e-06 | 31.88% | 46.80% | 1.47x | ✅ |
| `humanize_bytes[empty]` | 1.1593296983797467e-06 | 9.203057198689013e-07 | 20.62% | 25.97% | 1.26x | ✅ |
| `humanize_bytes[long]` | 4.259924965394089e-06 | 2.8442831300953704e-06 | 33.23% | 49.77% | 1.50x | ✅ |
| `humanize_bytes[short]` | 1.5455361202206072e-06 | 1.2118645287655216e-06 | 21.59% | 27.53% | 1.28x | ✅ |
| `humanize_hash[32-bytes]` | 4.660305992402445e-06 | 3.0414968458407182e-06 | 34.74% | 53.22% | 1.53x | ✅ |
| `humanize_hash[empty]` | 1.3371670938415957e-06 | 8.128882312363037e-07 | 39.21% | 64.50% | 1.64x | ✅ |
| `humanize_hash[long]` | 4.444699552178137e-06 | 2.816304313764124e-06 | 36.64% | 57.82% | 1.58x | ✅ |
| `humanize_hash[short]` | 1.7404957385266327e-06 | 1.188948169580101e-06 | 31.69% | 46.39% | 1.46x | ✅ |
| `humanize_hexstr[empty]` | 1.8844586091104844e-06 | 6.379077849955435e-07 | 66.15% | 195.41% | 2.95x | ✅ |
| `humanize_hexstr[short-0x]` | 4.823732869026541e-06 | 2.752907571404631e-06 | 42.93% | 75.22% | 1.75x | ✅ |
| `humanize_hexstr[short-no-0x]` | 4.048860871880553e-06 | 2.3367906642925828e-06 | 42.29% | 73.27% | 1.73x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.895035259846022e-06 | 2.835822758302901e-06 | 42.07% | 72.61% | 1.73x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 4.066472674377674e-06 | 2.3055480320878652e-06 | 43.30% | 76.38% | 1.76x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.108980548713171e-05 | 2.489957897535854e-05 | 19.91% | 24.86% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.731996073996797e-05 | 3.059842854846656e-05 | 18.01% | 21.97% | 1.22x | ✅ |
| `humanize_integer_sequence[empty]` | 9.242438104978809e-07 | 5.781317561372962e-07 | 37.45% | 59.87% | 1.60x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.6347679039090095e-05 | 3.8615912209885274e-05 | 16.68% | 20.02% | 1.20x | ✅ |
| `humanize_integer_sequence[single]` | 2.7136612815649926e-05 | 2.0536658151501266e-05 | 24.32% | 32.14% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.1014889247887996e-05 | 3.4046751170010646e-05 | 16.99% | 20.47% | 1.20x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.809304150370843e-05 | 6.761649203482868e-05 | 0.70% | 0.70% | 1.01x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9141797808708578e-05 | 1.825714277756811e-05 | 4.62% | 4.85% | 1.05x | ✅ |
| `humanize_seconds[negative]` | 2.4306926348233287e-05 | 1.791537009938717e-05 | 26.30% | 35.68% | 1.36x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7915939921892653e-05 | 2.0539237164906337e-05 | 26.42% | 35.92% | 1.36x | ✅ |
| `humanize_seconds[one-hour]` | 1.822783899115767e-05 | 1.685977314102667e-05 | 7.51% | 8.11% | 1.08x | ✅ |
| `humanize_seconds[one-minute]` | 1.8404901952358408e-05 | 1.7660452827642818e-05 | 4.04% | 4.22% | 1.04x | ✅ |
| `humanize_seconds[one-second]` | 1.912694091599603e-05 | 1.825322403276045e-05 | 4.57% | 4.79% | 1.05x | ✅ |
| `humanize_seconds[zero]` | 8.900563832942972e-07 | 7.722776005103465e-07 | 13.23% | 15.25% | 1.15x | ✅ |
| `humanize_wei[ether]` | 2.7385966530039126e-05 | 2.649986927962667e-05 | 3.24% | 3.34% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.71039389349183e-05 | 2.6145914827981236e-05 | 3.53% | 3.66% | 1.04x | ✅ |
| `humanize_wei[wei]` | 2.706532590679783e-05 | 2.564022874304848e-05 | 5.27% | 5.56% | 1.06x | ✅ |
| `humanize_wei[zero]` | 4.84162613407741e-06 | 3.7025370217443273e-06 | 23.53% | 30.77% | 1.31x | ✅ |
| `is_ipfs_uri[empty]` | 1.863708444138683e-05 | 1.8864064233986004e-05 | -1.22% | -1.20% | 0.99x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.361373853065885e-05 | 3.320818243246175e-05 | 1.21% | 1.22% | 1.01x | ✅ |
| `is_ipfs_uri[not-ipfs]` | 3.109592051773555e-05 | 3.154040485962992e-05 | -1.43% | -1.41% | 0.99x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.3985969137701365e-05 | 3.352850258717513e-05 | 1.35% | 1.36% | 1.01x | ✅ |
