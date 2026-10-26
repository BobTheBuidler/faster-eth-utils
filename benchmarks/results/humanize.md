#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.32804537240197e-06 | 2.6899230960016998e-06 | 37.85% | 60.90% | 1.61x | ✅ |
| `humanize_bytes[empty]` | 1.1674011022556356e-06 | 8.417473608703467e-07 | 27.90% | 38.69% | 1.39x | ✅ |
| `humanize_bytes[long]` | 4.032165845801679e-06 | 2.4907826713981676e-06 | 38.23% | 61.88% | 1.62x | ✅ |
| `humanize_bytes[short]` | 1.4647471347424998e-06 | 1.206420578111035e-06 | 17.64% | 21.41% | 1.21x | ✅ |
| `humanize_hash[32-bytes]` | 4.434149592200512e-06 | 2.6408978256979946e-06 | 40.44% | 67.90% | 1.68x | ✅ |
| `humanize_hash[empty]` | 1.299192504430925e-06 | 8.230289300783055e-07 | 36.65% | 57.86% | 1.58x | ✅ |
| `humanize_hash[long]` | 4.2366581701379115e-06 | 2.4498918445326525e-06 | 42.17% | 72.93% | 1.73x | ✅ |
| `humanize_hash[short]` | 1.6428450890902812e-06 | 1.1691301217556758e-06 | 28.84% | 40.52% | 1.41x | ✅ |
| `humanize_hexstr[empty]` | 1.8746751816521884e-06 | 6.650054656556905e-07 | 64.53% | 181.90% | 2.82x | ✅ |
| `humanize_hexstr[short-0x]` | 4.711732669454955e-06 | 2.4824173565690312e-06 | 47.31% | 89.80% | 1.90x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.978911684059262e-06 | 2.0417120192998416e-06 | 48.69% | 94.88% | 1.95x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.6548495338334515e-06 | 2.4897376769809242e-06 | 46.51% | 86.96% | 1.87x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.956132376739096e-06 | 2.039315456878063e-06 | 48.45% | 93.99% | 1.94x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.063436590426219e-05 | 2.4552497557213476e-05 | 19.85% | 24.77% | 1.25x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.717897691623411e-05 | 2.9790469016957295e-05 | 19.87% | 24.80% | 1.25x | ✅ |
| `humanize_integer_sequence[empty]` | 9.088786828907775e-07 | 5.967954955114963e-07 | 34.34% | 52.29% | 1.52x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.5844698884738374e-05 | 3.7073288439846215e-05 | 19.13% | 23.66% | 1.24x | ✅ |
| `humanize_integer_sequence[single]` | 2.6753317164634392e-05 | 2.0312240844065064e-05 | 24.08% | 31.71% | 1.32x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.097469067618203e-05 | 3.341894912376806e-05 | 18.44% | 22.61% | 1.23x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.933616403382214e-05 | 6.824429268512052e-05 | 1.57% | 1.60% | 1.02x | ✅ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9298537826867305e-05 | 1.6661131980975596e-05 | 13.67% | 15.83% | 1.16x | ✅ |
| `humanize_seconds[negative]` | 2.4250696994707935e-05 | 1.3947905025898721e-05 | 42.48% | 73.87% | 1.74x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.840462467680265e-05 | 1.6201674041038235e-05 | 42.96% | 75.32% | 1.75x | ✅ |
| `humanize_seconds[one-hour]` | 1.8225288805526212e-05 | 1.5470816755247855e-05 | 15.11% | 17.80% | 1.18x | ✅ |
| `humanize_seconds[one-minute]` | 1.853236323164774e-05 | 1.614444879391977e-05 | 12.89% | 14.79% | 1.15x | ✅ |
| `humanize_seconds[one-second]` | 1.9173595442124543e-05 | 1.6545401136543404e-05 | 13.71% | 15.88% | 1.16x | ✅ |
| `humanize_seconds[zero]` | 8.498960956101383e-07 | 8.088504634115764e-07 | 4.83% | 5.07% | 1.05x | ✅ |
| `humanize_wei[ether]` | 2.8243895621890738e-05 | 2.6793241078035467e-05 | 5.14% | 5.41% | 1.05x | ✅ |
| `humanize_wei[gwei]` | 2.797512716845388e-05 | 2.643778751333563e-05 | 5.50% | 5.81% | 1.06x | ✅ |
| `humanize_wei[wei]` | 2.838858395337218e-05 | 2.5951851304103687e-05 | 8.58% | 9.39% | 1.09x | ✅ |
| `humanize_wei[zero]` | 4.955561433674236e-06 | 3.175786106879565e-06 | 35.91% | 56.04% | 1.56x | ✅ |
| `is_ipfs_uri[empty]` | 1.884086164699854e-05 | 1.916600548178279e-05 | -1.73% | -1.70% | 0.98x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.387244517657615e-05 | 3.4165933742348485e-05 | -0.87% | -0.86% | 0.99x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.173620996415863e-05 | 3.2426400216560383e-05 | -2.17% | -2.13% | 0.98x | ❌ |
| `is_ipfs_uri[valid-cidv0]` | 3.4448353634437176e-05 | 3.4056942733617476e-05 | 1.14% | 1.15% | 1.01x | ✅ |
