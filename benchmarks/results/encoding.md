#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.192431465949704e-06 | 2.0006441323273142e-06 | 8.75% | 9.59% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5908013639873768e-06 | 1.5116073997799013e-06 | 4.98% | 5.24% | 1.05x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.90885760245633e-06 | 1.8305151015828325e-06 | 4.10% | 4.28% | 1.04x | ✅ |
| `big_endian_to_int[one-byte]` | 1.913223398058916e-06 | 1.7151807628574277e-06 | 10.35% | 11.55% | 1.12x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.90162365880885e-06 | 1.69372820209079e-06 | 10.93% | 12.27% | 1.12x | ✅ |
| `int_to_big_endian[255]` | 1.6539392459593691e-06 | 9.343976410327556e-07 | 43.50% | 77.01% | 1.77x | ✅ |
| `int_to_big_endian[256]` | 1.6504920185079434e-06 | 9.471294342571867e-07 | 42.62% | 74.26% | 1.74x | ✅ |
| `int_to_big_endian[max]` | 2.011214356444916e-06 | 1.1652501952470458e-06 | 42.06% | 72.60% | 1.73x | ✅ |
| `int_to_big_endian[one]` | 1.6447326260170636e-06 | 9.053918366924726e-07 | 44.95% | 81.66% | 1.82x | ✅ |
| `int_to_big_endian[zero]` | 1.7154734589633562e-06 | 1.0391174940144064e-06 | 39.43% | 65.09% | 1.65x | ✅ |
