#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3020189515930742e-06 | 2.0945226194867865e-06 | 9.01% | 9.91% | 1.10x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6334797491695045e-06 | 1.5398034752173938e-06 | 5.73% | 6.08% | 1.06x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9133288763643115e-06 | 1.7566735403743612e-06 | 8.19% | 8.92% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9250506018739252e-06 | 1.7677417568150698e-06 | 8.17% | 8.90% | 1.09x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.90886450003623e-06 | 1.754561755264592e-06 | 8.08% | 8.79% | 1.09x | ✅ |
| `int_to_big_endian[255]` | 1.6596328385322838e-06 | 8.911984380352712e-07 | 46.30% | 86.22% | 1.86x | ✅ |
| `int_to_big_endian[256]` | 1.6660924477819616e-06 | 9.035606751978456e-07 | 45.77% | 84.39% | 1.84x | ✅ |
| `int_to_big_endian[max]` | 2.029774171207673e-06 | 1.1905412764157696e-06 | 41.35% | 70.49% | 1.70x | ✅ |
| `int_to_big_endian[one]` | 1.654755814847177e-06 | 9.200165110267397e-07 | 44.40% | 79.86% | 1.80x | ✅ |
| `int_to_big_endian[zero]` | 1.7384152143314557e-06 | 1.0532337537142513e-06 | 39.41% | 65.06% | 1.65x | ✅ |
