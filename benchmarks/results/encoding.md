#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.2380834871290867e-06 | 1.9897567367756117e-06 | 11.10% | 12.48% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.666627825993229e-06 | 1.4478421822616146e-06 | 13.13% | 15.11% | 1.15x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.783636402953861e-06 | 1.5032085163868557e-06 | 15.72% | 18.66% | 1.19x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7839467393735329e-06 | 1.506399751874666e-06 | 15.56% | 18.42% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7772949814175466e-06 | 1.4957801218094202e-06 | 15.84% | 18.82% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.6342734782804046e-06 | 1.3445605756960127e-06 | 17.73% | 21.55% | 1.22x | ✅ |
| `int_to_big_endian[256]` | 1.6346547302590164e-06 | 1.3485125938134681e-06 | 17.50% | 21.22% | 1.21x | ✅ |
| `int_to_big_endian[max]` | 1.9143619920298977e-06 | 1.8807780371245157e-06 | 1.75% | 1.79% | 1.02x | ✅ |
| `int_to_big_endian[one]` | 1.6060444131399693e-06 | 1.3459063218285986e-06 | 16.20% | 19.33% | 1.19x | ✅ |
| `int_to_big_endian[zero]` | 1.705196377740148e-06 | 1.45561338664525e-06 | 14.64% | 17.15% | 1.17x | ✅ |
