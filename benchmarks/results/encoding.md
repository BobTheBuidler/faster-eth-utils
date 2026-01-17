#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.356997472175297e-06 | 2.1490896746000597e-06 | 8.82% | 9.67% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.8152849938303778e-06 | 1.6458581341748604e-06 | 9.33% | 10.29% | 1.10x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9256793727840202e-06 | 1.6961432367328231e-06 | 11.92% | 13.53% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9149676631000236e-06 | 1.7007980668938756e-06 | 11.18% | 12.59% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.910907633406792e-06 | 1.6890981516833991e-06 | 11.61% | 13.13% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.5648773484419075e-06 | 1.3812840118211389e-06 | 11.73% | 13.29% | 1.13x | ✅ |
| `int_to_big_endian[256]` | 1.5851743411808651e-06 | 1.3787539898823075e-06 | 13.02% | 14.97% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.942399565731805e-06 | 1.8320565666746598e-06 | 5.68% | 6.02% | 1.06x | ✅ |
| `int_to_big_endian[one]` | 1.568345105036605e-06 | 1.398264851817159e-06 | 10.84% | 12.16% | 1.12x | ✅ |
| `int_to_big_endian[zero]` | 1.6625587441703182e-06 | 1.4779858830294363e-06 | 11.10% | 12.49% | 1.12x | ✅ |
