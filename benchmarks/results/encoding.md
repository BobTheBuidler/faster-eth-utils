#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.328429362369556e-06 | 2.0664463499694336e-06 | 11.25% | 12.68% | 1.13x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7918122682017304e-06 | 1.544332855633069e-06 | 13.81% | 16.03% | 1.16x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.967006886391874e-06 | 1.6436131903346966e-06 | 16.44% | 19.68% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.943710325826948e-06 | 1.6515010572736328e-06 | 15.03% | 17.69% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9576107877477183e-06 | 1.6578623068253666e-06 | 15.31% | 18.08% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.5530417679600282e-06 | 1.347819195637189e-06 | 13.21% | 15.23% | 1.15x | ✅ |
| `int_to_big_endian[256]` | 1.5535956224340123e-06 | 1.3355143202014204e-06 | 14.04% | 16.33% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.928518086033845e-06 | 1.5883475839505688e-06 | 17.64% | 21.42% | 1.21x | ✅ |
| `int_to_big_endian[one]` | 1.566820838928896e-06 | 1.3297408807514987e-06 | 15.13% | 17.83% | 1.18x | ✅ |
| `int_to_big_endian[zero]` | 1.671050228288081e-06 | 1.444673168258711e-06 | 13.55% | 15.67% | 1.16x | ✅ |
