#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4458222232546064e-06 | 2.0835324161573164e-06 | 14.81% | 17.39% | 1.17x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7915943257951397e-06 | 1.6542923486325333e-06 | 7.66% | 8.30% | 1.08x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9659781183503167e-06 | 1.704619230041291e-06 | 13.29% | 15.33% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9609518394227095e-06 | 1.6984354123746313e-06 | 13.39% | 15.46% | 1.15x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9757358371434042e-06 | 1.71329860416839e-06 | 13.28% | 15.32% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5442354145014284e-06 | 1.3665662673887563e-06 | 11.51% | 13.00% | 1.13x | ✅ |
| `int_to_big_endian[256]` | 1.5428121917822958e-06 | 1.3694207669723656e-06 | 11.24% | 12.66% | 1.13x | ✅ |
| `int_to_big_endian[max]` | 1.9090166733308575e-06 | 1.7258332899810677e-06 | 9.60% | 10.61% | 1.11x | ✅ |
| `int_to_big_endian[one]` | 1.5686451315597122e-06 | 1.3665155536056228e-06 | 12.89% | 14.79% | 1.15x | ✅ |
| `int_to_big_endian[zero]` | 1.6771804323696926e-06 | 1.4988398259438222e-06 | 10.63% | 11.90% | 1.12x | ✅ |
