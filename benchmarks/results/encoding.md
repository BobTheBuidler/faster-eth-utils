#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.336707341800082e-06 | 2.1553250611241933e-06 | 7.76% | 8.42% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.736312902799492e-06 | 1.6566921382014583e-06 | 4.59% | 4.81% | 1.05x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9346010319763106e-06 | 1.7200969512451293e-06 | 11.09% | 12.47% | 1.12x | ✅ |
| `big_endian_to_int[one-byte]` | 1.939584072884054e-06 | 1.712987230298114e-06 | 11.68% | 13.23% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9374696540755608e-06 | 1.7085578285067067e-06 | 11.81% | 13.40% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.5596928787725257e-06 | 1.4045833918177236e-06 | 9.94% | 11.04% | 1.11x | ✅ |
| `int_to_big_endian[256]` | 1.554536910860042e-06 | 1.3981209409502233e-06 | 10.06% | 11.19% | 1.11x | ✅ |
| `int_to_big_endian[max]` | 1.946440148041802e-06 | 1.6802664673773248e-06 | 13.67% | 15.84% | 1.16x | ✅ |
| `int_to_big_endian[one]` | 1.5580619530527794e-06 | 1.395913288192057e-06 | 10.41% | 11.62% | 1.12x | ✅ |
| `int_to_big_endian[zero]` | 1.6973797057746606e-06 | 1.4966398218832344e-06 | 11.83% | 13.41% | 1.13x | ✅ |
