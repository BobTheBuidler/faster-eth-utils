#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/add-decimal_zero-constant-and-refactor-check/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.331663177151088e-06 | 2.017180263518066e-06 | 13.49% | 15.59% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7500723534831084e-06 | 1.5962479240519649e-06 | 8.79% | 9.64% | 1.10x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9300486214371527e-06 | 1.6817112223862154e-06 | 12.87% | 14.77% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8996815031656374e-06 | 1.6483564710818635e-06 | 13.23% | 15.25% | 1.15x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.8975247586481401e-06 | 1.6759572853274791e-06 | 11.68% | 13.22% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.5366041409173223e-06 | 1.3288167972206287e-06 | 13.52% | 15.64% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5293494895375582e-06 | 1.3232365588988253e-06 | 13.48% | 15.58% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.93247502149808e-06 | 1.6860798495975393e-06 | 12.75% | 14.61% | 1.15x | ✅ |
| `int_to_big_endian[one]` | 1.525427274804529e-06 | 1.3138039681138715e-06 | 13.87% | 16.11% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6482527800900222e-06 | 1.4056007948509952e-06 | 14.72% | 17.26% | 1.17x | ✅ |
