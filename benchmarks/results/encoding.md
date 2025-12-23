#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.0999618074451593e-06 | 1.8883962024303814e-06 | 10.07% | 11.20% | 1.11x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5747460514228308e-06 | 1.4787518568749486e-06 | 6.10% | 6.49% | 1.06x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7327821481242839e-06 | 1.5007435282814248e-06 | 13.39% | 15.46% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7361585139386984e-06 | 1.4964312648974012e-06 | 13.81% | 16.02% | 1.16x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7480930983230116e-06 | 1.5068320492640018e-06 | 13.80% | 16.01% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.4878036568095446e-06 | 1.3229897872810864e-06 | 11.08% | 12.46% | 1.12x | ✅ |
| `int_to_big_endian[256]` | 1.4896532327550889e-06 | 1.3111172866214709e-06 | 11.99% | 13.62% | 1.14x | ✅ |
| `int_to_big_endian[max]` | 1.8607753102205918e-06 | 1.6197806167294016e-06 | 12.95% | 14.88% | 1.15x | ✅ |
| `int_to_big_endian[one]` | 1.4816487238137682e-06 | 1.3151031331074761e-06 | 11.24% | 12.66% | 1.13x | ✅ |
| `int_to_big_endian[zero]` | 1.6070619477857062e-06 | 1.3889386037589836e-06 | 13.57% | 15.70% | 1.16x | ✅ |
