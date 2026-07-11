#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.290463909274034e-06 | 2.0869154416593862e-06 | 8.89% | 9.75% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.753963895398276e-06 | 1.6228245962114645e-06 | 7.48% | 8.08% | 1.08x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9520023523135735e-06 | 1.7998647419931118e-06 | 7.79% | 8.45% | 1.08x | ✅ |
| `big_endian_to_int[one-byte]` | 1.960075513354451e-06 | 1.7939360350154847e-06 | 8.48% | 9.26% | 1.09x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9021110480399882e-06 | 1.7697189240756858e-06 | 6.96% | 7.48% | 1.07x | ✅ |
| `int_to_big_endian[255]` | 1.5747815296719332e-06 | 9.020077111426916e-07 | 42.72% | 74.59% | 1.75x | ✅ |
| `int_to_big_endian[256]` | 1.572442900882404e-06 | 9.112276982341968e-07 | 42.05% | 72.56% | 1.73x | ✅ |
| `int_to_big_endian[max]` | 1.983376130822093e-06 | 1.1621675395029355e-06 | 41.40% | 70.66% | 1.71x | ✅ |
| `int_to_big_endian[one]` | 1.5526013405909765e-06 | 8.939986080531374e-07 | 42.42% | 73.67% | 1.74x | ✅ |
| `int_to_big_endian[zero]` | 1.6725070936966656e-06 | 1.038769475201743e-06 | 37.89% | 61.01% | 1.61x | ✅ |
