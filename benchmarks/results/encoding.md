#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.409342437973849e-06 | 2.1586378007280213e-06 | 10.41% | 11.61% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7554696661006157e-06 | 1.5793859745459265e-06 | 10.03% | 11.15% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9414965998172826e-06 | 1.6214161954950129e-06 | 16.49% | 19.74% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9346234370938803e-06 | 1.658484918836422e-06 | 14.27% | 16.65% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9412893772680455e-06 | 1.6457785597618157e-06 | 15.22% | 17.96% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.570889836242529e-06 | 1.3598015131364504e-06 | 13.44% | 15.52% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5688479673705786e-06 | 1.3589330400396314e-06 | 13.38% | 15.45% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 2.0214567034481725e-06 | 1.6609637229193172e-06 | 17.83% | 21.70% | 1.22x | ✅ |
| `int_to_big_endian[one]` | 1.6099354023775174e-06 | 1.3503980574211512e-06 | 16.12% | 19.22% | 1.19x | ✅ |
| `int_to_big_endian[zero]` | 1.7079086944018265e-06 | 1.4442482057353408e-06 | 15.44% | 18.26% | 1.18x | ✅ |
