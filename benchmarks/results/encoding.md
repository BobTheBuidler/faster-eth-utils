#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.148326414673018e-06 | 1.852292545478581e-06 | 13.78% | 15.98% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6692243572135984e-06 | 1.5029704652453613e-06 | 9.96% | 11.06% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7616954020426086e-06 | 1.5463195624317765e-06 | 12.23% | 13.93% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.752328781822787e-06 | 1.663050592463474e-06 | 5.09% | 5.37% | 1.05x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7422003344654325e-06 | 1.5329770938464203e-06 | 12.01% | 13.65% | 1.14x | ✅ |
| `int_to_big_endian[255]` | 1.5486838418165898e-06 | 1.75026380069256e-06 | -13.02% | -11.52% | 0.88x | ❌ |
| `int_to_big_endian[256]` | 1.5452762907895349e-06 | 1.7124801657785256e-06 | -10.82% | -9.76% | 0.90x | ❌ |
| `int_to_big_endian[max]` | 1.9071466235779483e-06 | 2.1231025005971407e-06 | -11.32% | -10.17% | 0.90x | ❌ |
| `int_to_big_endian[one]` | 1.5567228694587758e-06 | 1.738764432576658e-06 | -11.69% | -10.47% | 0.90x | ❌ |
| `int_to_big_endian[zero]` | 1.679211744071038e-06 | 1.8013269460507397e-06 | -7.27% | -6.78% | 0.93x | ❌ |
