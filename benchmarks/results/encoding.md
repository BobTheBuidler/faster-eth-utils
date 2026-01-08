#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3569594522513138e-06 | 2.128140999468164e-06 | 9.71% | 10.75% | 1.11x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7780240891993539e-06 | 1.596217620545818e-06 | 10.23% | 11.39% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9350391295330557e-06 | 1.6976722760738654e-06 | 12.27% | 13.98% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9303885487079825e-06 | 1.6907671014195968e-06 | 12.41% | 14.17% | 1.14x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9466708791957293e-06 | 1.698190896248232e-06 | 12.76% | 14.63% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5665827342213164e-06 | 1.3682448718147562e-06 | 12.66% | 14.50% | 1.14x | ✅ |
| `int_to_big_endian[256]` | 1.5592609662283555e-06 | 1.3539012830162374e-06 | 13.17% | 15.17% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.9299090358572657e-06 | 1.6417034537623079e-06 | 14.93% | 17.56% | 1.18x | ✅ |
| `int_to_big_endian[one]` | 1.5669994162978058e-06 | 1.3559648759948698e-06 | 13.47% | 15.56% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6653122805264937e-06 | 1.3443437150381904e-06 | 19.27% | 23.88% | 1.24x | ✅ |
