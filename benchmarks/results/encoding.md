#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3539001259985802e-06 | 2.0272617915363163e-06 | 13.88% | 16.11% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7582119435011678e-06 | 1.56856009756508e-06 | 10.79% | 12.09% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.913325121407622e-06 | 1.6603690147185387e-06 | 13.22% | 15.23% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9279446993566198e-06 | 1.643059080761387e-06 | 14.78% | 17.34% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.922246032220089e-06 | 1.632423362853665e-06 | 15.08% | 17.75% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.5458361968312556e-06 | 1.3582851724443408e-06 | 12.13% | 13.81% | 1.14x | ✅ |
| `int_to_big_endian[256]` | 1.5325825622244044e-06 | 1.3545665078131407e-06 | 11.62% | 13.14% | 1.13x | ✅ |
| `int_to_big_endian[max]` | 1.9431277848939464e-06 | 1.664452524978507e-06 | 14.34% | 16.74% | 1.17x | ✅ |
| `int_to_big_endian[one]` | 1.5247460816107952e-06 | 1.3276190815679649e-06 | 12.93% | 14.85% | 1.15x | ✅ |
| `int_to_big_endian[zero]` | 1.6721477260536123e-06 | 1.423829889262805e-06 | 14.85% | 17.44% | 1.17x | ✅ |
