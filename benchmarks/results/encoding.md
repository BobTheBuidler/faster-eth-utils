#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-utils-6.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4261800465105127e-06 | 2.0648397535513556e-06 | 14.89% | 17.50% | 1.17x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7777730577747045e-06 | 1.5560559254871902e-06 | 12.47% | 14.25% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.921582466792066e-06 | 1.5849292771617328e-06 | 17.52% | 21.24% | 1.21x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8950045962527906e-06 | 1.5884547606119694e-06 | 16.18% | 19.30% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.939721719909512e-06 | 1.5916037187854791e-06 | 17.95% | 21.87% | 1.22x | ✅ |
| `int_to_big_endian[255]` | 1.58528869243525e-06 | 1.4327152863702642e-06 | 9.62% | 10.65% | 1.11x | ✅ |
| `int_to_big_endian[256]` | 1.5618776747439712e-06 | 1.4102874084104865e-06 | 9.71% | 10.75% | 1.11x | ✅ |
| `int_to_big_endian[max]` | 2.060909563295521e-06 | 1.8215321983066098e-06 | 11.62% | 13.14% | 1.13x | ✅ |
| `int_to_big_endian[one]` | 1.566401284333296e-06 | 1.4245022299592002e-06 | 9.06% | 9.96% | 1.10x | ✅ |
| `int_to_big_endian[zero]` | 1.734055116586326e-06 | 1.520122995720867e-06 | 12.34% | 14.07% | 1.14x | ✅ |
