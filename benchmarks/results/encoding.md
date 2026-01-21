#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3727105652019325e-06 | 2.155276180618901e-06 | 9.16% | 10.09% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.896308565447474e-06 | 1.5726377692714252e-06 | 17.07% | 20.58% | 1.21x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9396896202935963e-06 | 1.7610408361128348e-06 | 9.21% | 10.14% | 1.10x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9071608115858135e-06 | 1.6432080766338333e-06 | 13.84% | 16.06% | 1.16x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.923657501656845e-06 | 1.6369024955849292e-06 | 14.91% | 17.52% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.548858611562019e-06 | 1.3413892062316879e-06 | 13.39% | 15.47% | 1.15x | ✅ |
| `int_to_big_endian[256]` | 1.571314125149642e-06 | 1.3482108826404443e-06 | 14.20% | 16.55% | 1.17x | ✅ |
| `int_to_big_endian[max]` | 2.0070201657072177e-06 | 1.6779773091149053e-06 | 16.39% | 19.61% | 1.20x | ✅ |
| `int_to_big_endian[one]` | 1.5390178769803742e-06 | 1.3506957931834848e-06 | 12.24% | 13.94% | 1.14x | ✅ |
| `int_to_big_endian[zero]` | 1.6795966693846816e-06 | 1.432265559514847e-06 | 14.73% | 17.27% | 1.17x | ✅ |
