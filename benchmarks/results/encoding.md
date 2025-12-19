#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.329085020714198e-06 | 1.961856064252251e-06 | 15.77% | 18.72% | 1.19x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.742356819808856e-06 | 1.5233063752066058e-06 | 12.57% | 14.38% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9217686556594654e-06 | 1.6020461775881682e-06 | 16.64% | 19.96% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9177258650211542e-06 | 1.5912428653048604e-06 | 17.02% | 20.52% | 1.21x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9077019354988206e-06 | 1.6844523092271918e-06 | 11.70% | 13.25% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.5535158105718305e-06 | 1.3436478544493282e-06 | 13.51% | 15.62% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5774124169146034e-06 | 1.3316417667754908e-06 | 15.58% | 18.46% | 1.18x | ✅ |
| `int_to_big_endian[max]` | 1.940367849827646e-06 | 1.77548416468221e-06 | 8.50% | 9.29% | 1.09x | ✅ |
| `int_to_big_endian[one]` | 1.6687409913040693e-06 | 1.3742913150762796e-06 | 17.65% | 21.43% | 1.21x | ✅ |
| `int_to_big_endian[zero]` | 1.6680680710669837e-06 | 1.4187072413498898e-06 | 14.95% | 17.58% | 1.18x | ✅ |
