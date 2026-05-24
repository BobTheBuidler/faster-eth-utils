#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.0484258546458174e-06 | 1.8581005456850023e-06 | 9.29% | 10.24% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7429763421743262e-06 | 1.5604980095040386e-06 | 10.47% | 11.69% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8103420708463394e-06 | 1.6196024133707723e-06 | 10.54% | 11.78% | 1.12x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8012101806050378e-06 | 1.6294895669641684e-06 | 9.53% | 10.54% | 1.11x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.785371759472402e-06 | 1.656154208101056e-06 | 7.24% | 7.80% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.5242318963930513e-06 | 9.417840899552964e-07 | 38.21% | 61.85% | 1.62x | ✅ |
| `int_to_big_endian[256]` | 1.5305752065213374e-06 | 9.24472289567021e-07 | 39.60% | 65.56% | 1.66x | ✅ |
| `int_to_big_endian[max]` | 1.892922818493205e-06 | 1.1276959928136424e-06 | 40.43% | 67.86% | 1.68x | ✅ |
| `int_to_big_endian[one]` | 1.5370960878497299e-06 | 9.310678360165517e-07 | 39.43% | 65.09% | 1.65x | ✅ |
| `int_to_big_endian[zero]` | 1.6752987775117119e-06 | 1.0207765900983128e-06 | 39.07% | 64.12% | 1.64x | ✅ |
