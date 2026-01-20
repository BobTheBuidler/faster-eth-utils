#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3379682815887988e-06 | 2.0267999095113807e-06 | 13.31% | 15.35% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.755375645766814e-06 | 1.5383255766618662e-06 | 12.36% | 14.11% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9211584483986645e-06 | 1.6312414269178412e-06 | 15.09% | 17.77% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9336748354307977e-06 | 1.6308216307040525e-06 | 15.66% | 18.57% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9241227423762233e-06 | 1.6384516526266661e-06 | 14.85% | 17.44% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.6447025631841746e-06 | 1.3552252143643194e-06 | 17.60% | 21.36% | 1.21x | ✅ |
| `int_to_big_endian[256]` | 1.6267655257211863e-06 | 1.3579237113367476e-06 | 16.53% | 19.80% | 1.20x | ✅ |
| `int_to_big_endian[max]` | 2.00277243928753e-06 | 1.661858272215335e-06 | 17.02% | 20.51% | 1.21x | ✅ |
| `int_to_big_endian[one]` | 1.6318630933554727e-06 | 1.3559238252994117e-06 | 16.91% | 20.35% | 1.20x | ✅ |
| `int_to_big_endian[zero]` | 1.7801832973696663e-06 | 1.4368639004243473e-06 | 19.29% | 23.89% | 1.24x | ✅ |
