#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.341158530310278e-06 | 2.032922739400701e-06 | 13.17% | 15.16% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7786976043089322e-06 | 1.5628847125955848e-06 | 12.13% | 13.81% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.939799533032213e-06 | 1.6604615618401983e-06 | 14.40% | 16.82% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9284097774849804e-06 | 1.6451117860750195e-06 | 14.69% | 17.22% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.93803339614597e-06 | 1.6321146084595624e-06 | 15.79% | 18.74% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5666408574101067e-06 | 1.3508908755117382e-06 | 13.77% | 15.97% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5533802697738293e-06 | 1.3485396349613749e-06 | 13.19% | 15.19% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.945655410073008e-06 | 1.6581325319048211e-06 | 14.78% | 17.34% | 1.17x | ✅ |
| `int_to_big_endian[one]` | 1.5623874053289465e-06 | 1.340803818621576e-06 | 14.18% | 16.53% | 1.17x | ✅ |
| `int_to_big_endian[zero]` | 1.7001326491319703e-06 | 1.4200175900399637e-06 | 16.48% | 19.73% | 1.20x | ✅ |
