#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1548338416031357e-06 | 1.8762019462036392e-06 | 12.93% | 14.85% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6726481506996635e-06 | 1.3579793241948914e-06 | 18.81% | 23.17% | 1.23x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7767676306570131e-06 | 1.516753537186708e-06 | 14.63% | 17.14% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7714725619188535e-06 | 1.4898458637062084e-06 | 15.90% | 18.90% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7596352285891325e-06 | 1.5167728297755764e-06 | 13.80% | 16.01% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.5752988293651274e-06 | 1.697932240618272e-06 | -7.78% | -7.22% | 0.93x | ❌ |
| `int_to_big_endian[256]` | 1.5684401576489792e-06 | 1.6731216499851823e-06 | -6.67% | -6.26% | 0.94x | ❌ |
| `int_to_big_endian[max]` | 1.9260069489822275e-06 | 1.9823570516079486e-06 | -2.93% | -2.84% | 0.97x | ❌ |
| `int_to_big_endian[one]` | 1.5907366136027063e-06 | 1.6905959597382568e-06 | -6.28% | -5.91% | 0.94x | ❌ |
| `int_to_big_endian[zero]` | 1.6698518141983493e-06 | 1.7493964153489455e-06 | -4.76% | -4.55% | 0.95x | ❌ |
