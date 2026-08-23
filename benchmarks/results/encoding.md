#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.151545405602158e-06 | 1.9772009615019656e-06 | 8.10% | 8.82% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5166645638904064e-06 | 1.5592931545602164e-06 | -2.81% | -2.73% | 0.97x | ❌ |
| `big_endian_to_int[ff-byte]` | 1.7950653390344485e-06 | 1.7529237180665125e-06 | 2.35% | 2.40% | 1.02x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7722132576305121e-06 | 1.735015124770234e-06 | 2.10% | 2.14% | 1.02x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7794787074214252e-06 | 1.7422199093254372e-06 | 2.09% | 2.14% | 1.02x | ✅ |
| `int_to_big_endian[255]` | 1.5403204723965756e-06 | 9.297664324519472e-07 | 39.64% | 65.67% | 1.66x | ✅ |
| `int_to_big_endian[256]` | 1.4483570286723484e-06 | 9.408344355597144e-07 | 35.04% | 53.94% | 1.54x | ✅ |
| `int_to_big_endian[max]` | 1.926092359239919e-06 | 1.1296716569950698e-06 | 41.35% | 70.50% | 1.71x | ✅ |
| `int_to_big_endian[one]` | 1.5318268060565485e-06 | 9.148684010320014e-07 | 40.28% | 67.44% | 1.67x | ✅ |
| `int_to_big_endian[zero]` | 1.6727463422457288e-06 | 1.0234705891932725e-06 | 38.81% | 63.44% | 1.63x | ✅ |
