#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.105706610484507e-06 | 1.923843646053782e-06 | 8.64% | 9.45% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6048866373219333e-06 | 1.5560938208300117e-06 | 3.04% | 3.14% | 1.03x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7740187656411174e-06 | 1.6152299657453415e-06 | 8.95% | 9.83% | 1.10x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8406175936407747e-06 | 1.6433151925852456e-06 | 10.72% | 12.01% | 1.12x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.772420556382828e-06 | 1.6426994326049895e-06 | 7.32% | 7.90% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.4620985172135467e-06 | 9.162418114009067e-07 | 37.33% | 59.58% | 1.60x | ✅ |
| `int_to_big_endian[256]` | 1.4541019098268795e-06 | 9.074039209042928e-07 | 37.60% | 60.25% | 1.60x | ✅ |
| `int_to_big_endian[max]` | 1.8550575686546794e-06 | 1.1174146078976781e-06 | 39.76% | 66.01% | 1.66x | ✅ |
| `int_to_big_endian[one]` | 1.4784261333993624e-06 | 9.284304445332842e-07 | 37.20% | 59.24% | 1.59x | ✅ |
| `int_to_big_endian[zero]` | 1.6724449979667737e-06 | 1.0332955769247819e-06 | 38.22% | 61.86% | 1.62x | ✅ |
