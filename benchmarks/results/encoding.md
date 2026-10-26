#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.363916560938233e-06 | 2.185591552486729e-06 | 7.54% | 8.16% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.835931077942439e-06 | 1.67522360187059e-06 | 8.75% | 9.59% | 1.10x | ✅ |
| `big_endian_to_int[ff-byte]` | 2.0880391162545903e-06 | 1.8121544201091938e-06 | 13.21% | 15.22% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 2.1149657447227735e-06 | 1.8181271027262467e-06 | 14.04% | 16.33% | 1.16x | ✅ |
| `big_endian_to_int[two-bytes]` | 2.092899291982316e-06 | 1.8460375478530076e-06 | 11.80% | 13.37% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.4868667292043903e-06 | 9.739177451816765e-07 | 34.50% | 52.67% | 1.53x | ✅ |
| `int_to_big_endian[256]` | 1.475688761796377e-06 | 9.59467846078065e-07 | 34.98% | 53.80% | 1.54x | ✅ |
| `int_to_big_endian[max]` | 1.8382664105471337e-06 | 1.1479015052845272e-06 | 37.56% | 60.14% | 1.60x | ✅ |
| `int_to_big_endian[one]` | 1.4633685432749799e-06 | 9.590256520847187e-07 | 34.46% | 52.59% | 1.53x | ✅ |
| `int_to_big_endian[zero]` | 1.6282489587286881e-06 | 1.0824856006492176e-06 | 33.52% | 50.42% | 1.50x | ✅ |
