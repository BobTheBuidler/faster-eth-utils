#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/refactor-get_normalized_abi_inputs-function/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3688794592074507e-06 | 2.0523528496234323e-06 | 13.36% | 15.42% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7838632242641087e-06 | 1.5319638267054867e-06 | 14.12% | 16.44% | 1.16x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.944896006333089e-06 | 1.716100577006919e-06 | 11.76% | 13.33% | 1.13x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9311614244657056e-06 | 1.8199106362383171e-06 | 5.76% | 6.11% | 1.06x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.928293969777115e-06 | 1.6255065366556591e-06 | 15.70% | 18.63% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5368484014280714e-06 | 1.3316056076916316e-06 | 13.35% | 15.41% | 1.15x | ✅ |
| `int_to_big_endian[256]` | 1.5383119681436487e-06 | 1.3355516064667738e-06 | 13.18% | 15.18% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 2.004049177383327e-06 | 1.6922541068211091e-06 | 15.56% | 18.42% | 1.18x | ✅ |
| `int_to_big_endian[one]` | 1.5168123475348526e-06 | 1.3312642350846176e-06 | 12.23% | 13.94% | 1.14x | ✅ |
| `int_to_big_endian[zero]` | 1.6780242224374513e-06 | 1.4346583016974576e-06 | 14.50% | 16.96% | 1.17x | ✅ |
