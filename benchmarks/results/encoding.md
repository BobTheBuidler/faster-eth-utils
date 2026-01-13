#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3331372192347177e-06 | 2.135540474693745e-06 | 8.47% | 9.25% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.8880175021252738e-06 | 1.5698062358935158e-06 | 16.85% | 20.27% | 1.20x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.940315025909327e-06 | 1.6691449464912707e-06 | 13.98% | 16.25% | 1.16x | ✅ |
| `big_endian_to_int[one-byte]` | 1.942946103792786e-06 | 1.658585683128165e-06 | 14.64% | 17.14% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9472129930911896e-06 | 1.6453732348681957e-06 | 15.50% | 18.34% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.5505106097923511e-06 | 1.3549848696233424e-06 | 12.61% | 14.43% | 1.14x | ✅ |
| `int_to_big_endian[256]` | 1.5536114847683821e-06 | 1.3497756788263357e-06 | 13.12% | 15.10% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.935026692238458e-06 | 1.7746369853679468e-06 | 8.29% | 9.04% | 1.09x | ✅ |
| `int_to_big_endian[one]` | 1.5478265119685864e-06 | 1.3411574242565283e-06 | 13.35% | 15.41% | 1.15x | ✅ |
| `int_to_big_endian[zero]` | 1.6936292455383842e-06 | 1.4378098202374185e-06 | 15.10% | 17.79% | 1.18x | ✅ |
