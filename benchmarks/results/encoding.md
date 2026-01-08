#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-address-equality-check-in-is_same_address/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.332155634218677e-06 | 2.1901645327550277e-06 | 6.09% | 6.48% | 1.06x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7504280119601951e-06 | 1.5844064070630727e-06 | 9.48% | 10.48% | 1.10x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9356328785560155e-06 | 1.675876541576456e-06 | 13.42% | 15.50% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9083025190069825e-06 | 1.682127563859873e-06 | 11.85% | 13.45% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9159817754213904e-06 | 1.6893361453033193e-06 | 11.83% | 13.42% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.5552364207885584e-06 | 1.3636861137001364e-06 | 12.32% | 14.05% | 1.14x | ✅ |
| `int_to_big_endian[256]` | 1.5566384268591666e-06 | 1.3244706822764715e-06 | 14.91% | 17.53% | 1.18x | ✅ |
| `int_to_big_endian[max]` | 1.9829350476955986e-06 | 1.6991606767446796e-06 | 14.31% | 16.70% | 1.17x | ✅ |
| `int_to_big_endian[one]` | 1.572069793679178e-06 | 1.3596670070825477e-06 | 13.51% | 15.62% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.679792077562948e-06 | 1.4517270472331087e-06 | 13.58% | 15.71% | 1.16x | ✅ |
