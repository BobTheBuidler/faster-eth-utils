#### [faster_eth_utils.humanize](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/humanize.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_humanize_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `humanize_bytes[32-bytes]` | 4.237275520782249e-06 | 2.516770006925783e-06 | 40.60% | 68.36% | 1.68x | ✅ |
| `humanize_bytes[empty]` | 1.1865731525123116e-06 | 8.38471153603774e-07 | 29.34% | 41.52% | 1.42x | ✅ |
| `humanize_bytes[long]` | 4.037278372653669e-06 | 2.3321111659864286e-06 | 42.24% | 73.12% | 1.73x | ✅ |
| `humanize_bytes[short]` | 1.5085139269052834e-06 | 1.2195276575890873e-06 | 19.16% | 23.70% | 1.24x | ✅ |
| `humanize_hash[32-bytes]` | 4.445412487879961e-06 | 2.515889290142474e-06 | 43.40% | 76.69% | 1.77x | ✅ |
| `humanize_hash[empty]` | 1.3883717294618402e-06 | 8.705113506810781e-07 | 37.30% | 59.49% | 1.59x | ✅ |
| `humanize_hash[long]` | 4.286810451024409e-06 | 2.3402178133154022e-06 | 45.41% | 83.18% | 1.83x | ✅ |
| `humanize_hash[short]` | 1.7687536362810568e-06 | 1.2368070453446926e-06 | 30.07% | 43.01% | 1.43x | ✅ |
| `humanize_hexstr[empty]` | 1.9613353059544005e-06 | 6.710149886415536e-07 | 65.79% | 192.29% | 2.92x | ✅ |
| `humanize_hexstr[short-0x]` | 4.814695799990095e-06 | 2.4288155343850063e-06 | 49.55% | 98.23% | 1.98x | ✅ |
| `humanize_hexstr[short-no-0x]` | 3.998921435557585e-06 | 1.964959124100598e-06 | 50.86% | 103.51% | 2.04x | ✅ |
| `humanize_hexstr[very-long-0x]` | 4.776758404624452e-06 | 2.4133494729781364e-06 | 49.48% | 97.93% | 1.98x | ✅ |
| `humanize_hexstr[very-long-no-0x]` | 3.9945284103649865e-06 | 1.978615229569369e-06 | 50.47% | 101.89% | 2.02x | ✅ |
| `humanize_integer_sequence[consecutive]` | 3.151519907391487e-05 | 2.3442516213067375e-05 | 25.62% | 34.44% | 1.34x | ✅ |
| `humanize_integer_sequence[disjoint]` | 3.747805689167715e-05 | 2.9139243042760112e-05 | 22.25% | 28.62% | 1.29x | ✅ |
| `humanize_integer_sequence[empty]` | 9.370422326243486e-07 | 7.252987727409257e-07 | 22.60% | 29.19% | 1.29x | ✅ |
| `humanize_integer_sequence[mixed]` | 4.610188177682099e-05 | 3.607932905175912e-05 | 21.74% | 27.78% | 1.28x | ✅ |
| `humanize_integer_sequence[single]` | 2.7338884559569053e-05 | 1.9320079815346076e-05 | 29.33% | 41.51% | 1.42x | ✅ |
| `humanize_integer_sequence[two-consecutive-ranges]` | 4.127173300751631e-05 | 3.21856186633506e-05 | 22.02% | 28.23% | 1.28x | ✅ |
| `humanize_ipfs_uri[valid-cidv0]` | 6.837684736274084e-05 | 6.928500736288943e-05 | -1.33% | -1.31% | 0.99x | ❌ |
| `humanize_seconds[fifty-nine-seconds]` | 1.9202677651848332e-05 | 1.5594654627755205e-05 | 18.79% | 23.14% | 1.23x | ✅ |
| `humanize_seconds[negative]` | 2.315198680864538e-05 | 1.2752889512755626e-05 | 44.92% | 81.54% | 1.82x | ✅ |
| `humanize_seconds[one-hour-one-minute-one-second]` | 2.7543661558227735e-05 | 1.4774666073411984e-05 | 46.36% | 86.42% | 1.86x | ✅ |
| `humanize_seconds[one-hour]` | 1.7879237832888098e-05 | 1.388179333610457e-05 | 22.36% | 28.80% | 1.29x | ✅ |
| `humanize_seconds[one-minute]` | 1.7955481322032666e-05 | 1.4741480508335153e-05 | 17.90% | 21.80% | 1.22x | ✅ |
| `humanize_seconds[one-second]` | 1.9489366198249332e-05 | 1.534502672457536e-05 | 21.26% | 27.01% | 1.27x | ✅ |
| `humanize_seconds[zero]` | 8.606932996304323e-07 | 8.204858198053039e-07 | 4.67% | 4.90% | 1.05x | ✅ |
| `humanize_wei[ether]` | 2.7727698138424167e-05 | 2.682349648430695e-05 | 3.26% | 3.37% | 1.03x | ✅ |
| `humanize_wei[gwei]` | 2.7932324786376914e-05 | 2.710950479872234e-05 | 2.95% | 3.04% | 1.03x | ✅ |
| `humanize_wei[wei]` | 2.7395385035252763e-05 | 2.653280503623614e-05 | 3.15% | 3.25% | 1.03x | ✅ |
| `humanize_wei[zero]` | 4.719161666655328e-06 | 2.998239442770953e-06 | 36.47% | 57.40% | 1.57x | ✅ |
| `is_ipfs_uri[empty]` | 1.8486929141086253e-05 | 1.8521137379917695e-05 | -0.19% | -0.18% | 1.00x | ❌ |
| `is_ipfs_uri[invalid-cid]` | 3.36336748944128e-05 | 3.3723917291356177e-05 | -0.27% | -0.27% | 1.00x | ❌ |
| `is_ipfs_uri[not-ipfs]` | 3.177428244160263e-05 | 3.1541726911688505e-05 | 0.73% | 0.74% | 1.01x | ✅ |
| `is_ipfs_uri[valid-cidv0]` | 3.408470900432104e-05 | 3.3985816718186306e-05 | 0.29% | 0.29% | 1.00x | ✅ |
