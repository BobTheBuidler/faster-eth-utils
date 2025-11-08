#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1600172997388756e-06 | 1.8867564436628613e-06 | 12.65% | 14.48% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6576325308494515e-06 | 1.439103783892148e-06 | 13.18% | 15.19% | 1.15x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7814685399954434e-06 | 1.513503619299179e-06 | 15.04% | 17.70% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.785394072640877e-06 | 1.5098519523759254e-06 | 15.43% | 18.25% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7561921127601403e-06 | 1.4964897398367823e-06 | 14.79% | 17.35% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.6591637703971011e-06 | 1.2566859443481856e-06 | 24.26% | 32.03% | 1.32x | ✅ |
| `int_to_big_endian[256]` | 1.5788549364659901e-06 | 1.2482832123770227e-06 | 20.94% | 26.48% | 1.26x | ✅ |
| `int_to_big_endian[max]` | 1.9041339565465976e-06 | 1.4496654155488383e-06 | 23.87% | 31.35% | 1.31x | ✅ |
| `int_to_big_endian[one]` | 1.5717798521795256e-06 | 1.2435808556487094e-06 | 20.88% | 26.39% | 1.26x | ✅ |
| `int_to_big_endian[zero]` | 1.65689701075572e-06 | 1.2248672886435035e-06 | 26.07% | 35.27% | 1.35x | ✅ |
