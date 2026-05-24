#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.2076844756500886e-06 | 2.0728063680409554e-06 | 6.11% | 6.51% | 1.07x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5950799819888137e-06 | 1.5126373355794814e-06 | 5.17% | 5.45% | 1.05x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.884154297798765e-06 | 1.7220385163842264e-06 | 8.60% | 9.41% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 1.877661442611029e-06 | 1.6651778066775426e-06 | 11.32% | 12.76% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9040909134096292e-06 | 1.677177708149704e-06 | 11.92% | 13.53% | 1.14x | ✅ |
| `int_to_big_endian[255]` | 1.6109111258313655e-06 | 8.890926914006376e-07 | 44.81% | 81.19% | 1.81x | ✅ |
| `int_to_big_endian[256]` | 1.6151493969997738e-06 | 8.876372934058468e-07 | 45.04% | 81.96% | 1.82x | ✅ |
| `int_to_big_endian[max]` | 1.999265056668783e-06 | 1.166386839606696e-06 | 41.66% | 71.41% | 1.71x | ✅ |
| `int_to_big_endian[one]` | 1.625123476890285e-06 | 8.807877902315286e-07 | 45.80% | 84.51% | 1.85x | ✅ |
| `int_to_big_endian[zero]` | 1.691649606689116e-06 | 1.0017089689725903e-06 | 40.79% | 68.88% | 1.69x | ✅ |
