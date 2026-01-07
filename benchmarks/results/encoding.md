#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3584332631599145e-06 | 2.168517176554055e-06 | 8.05% | 8.76% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7634950333383412e-06 | 1.5353023157989335e-06 | 12.94% | 14.86% | 1.15x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9282635975077228e-06 | 1.7629020276801638e-06 | 8.58% | 9.38% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 2.009211752246334e-06 | 1.628468474230325e-06 | 18.95% | 23.38% | 1.23x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9220197957978067e-06 | 1.7443603870526268e-06 | 9.24% | 10.18% | 1.10x | ✅ |
| `int_to_big_endian[255]` | 1.5244022238163355e-06 | 1.3486820045111088e-06 | 11.53% | 13.03% | 1.13x | ✅ |
| `int_to_big_endian[256]` | 1.5126034572277954e-06 | 1.351714771175153e-06 | 10.64% | 11.90% | 1.12x | ✅ |
| `int_to_big_endian[max]` | 1.9092749544034444e-06 | 1.7171953070437e-06 | 10.06% | 11.19% | 1.11x | ✅ |
| `int_to_big_endian[one]` | 1.5871962613904273e-06 | 1.3444202542281475e-06 | 15.30% | 18.06% | 1.18x | ✅ |
| `int_to_big_endian[zero]` | 1.690846089801031e-06 | 1.4431161428455255e-06 | 14.65% | 17.17% | 1.17x | ✅ |
