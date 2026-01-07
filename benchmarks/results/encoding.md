#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1375097654754028e-06 | 1.877362341233003e-06 | 12.17% | 13.86% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5499050798827988e-06 | 1.4207503648566766e-06 | 8.33% | 9.09% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7219052837269785e-06 | 1.4946224124289888e-06 | 13.20% | 15.21% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7260318570712134e-06 | 1.4809574911378478e-06 | 14.20% | 16.55% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.733893470594631e-06 | 1.4937154911325932e-06 | 13.85% | 16.08% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.4882664695870396e-06 | 1.4109293408063184e-06 | 5.20% | 5.48% | 1.05x | ✅ |
| `int_to_big_endian[256]` | 1.5034334517519154e-06 | 1.3849770245417586e-06 | 7.88% | 8.55% | 1.09x | ✅ |
| `int_to_big_endian[max]` | 1.8739532892878403e-06 | 1.723184581564889e-06 | 8.05% | 8.75% | 1.09x | ✅ |
| `int_to_big_endian[one]` | 1.479347033670349e-06 | 1.3951086602870354e-06 | 5.69% | 6.04% | 1.06x | ✅ |
| `int_to_big_endian[zero]` | 1.6114078051213696e-06 | 1.4329273682219432e-06 | 11.08% | 12.46% | 1.12x | ✅ |
