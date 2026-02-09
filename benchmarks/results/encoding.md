#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3261812192409695e-06 | 1.914329347094897e-06 | 17.71% | 21.51% | 1.22x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.752825199213777e-06 | 1.5244128895570839e-06 | 13.03% | 14.98% | 1.15x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9130401867473834e-06 | 1.6108997249331886e-06 | 15.79% | 18.76% | 1.19x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9178957384811955e-06 | 1.6167405358392882e-06 | 15.70% | 18.63% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9429552357567064e-06 | 1.719805467710053e-06 | 11.49% | 12.98% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.547456577061791e-06 | 1.3351776416895298e-06 | 13.72% | 15.90% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5351441278298905e-06 | 1.3442785533624645e-06 | 12.43% | 14.20% | 1.14x | ✅ |
| `int_to_big_endian[max]` | 1.9285245621796487e-06 | 1.7227445820165432e-06 | 10.67% | 11.94% | 1.12x | ✅ |
| `int_to_big_endian[one]` | 1.5459021737714724e-06 | 1.3288864483793484e-06 | 14.04% | 16.33% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6830989132571412e-06 | 1.4416274316463848e-06 | 14.35% | 16.75% | 1.17x | ✅ |
