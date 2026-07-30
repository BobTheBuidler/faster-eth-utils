#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.0695500659920357e-06 | 2.0224797614812785e-06 | 2.27% | 2.33% | 1.02x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5963164943008491e-06 | 1.5815441402114879e-06 | 0.93% | 0.93% | 1.01x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7255738807282035e-06 | 1.6235078957232564e-06 | 5.91% | 6.29% | 1.06x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7448966950006802e-06 | 1.6324436852321446e-06 | 6.44% | 6.89% | 1.07x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7240290089432198e-06 | 1.5838353007597199e-06 | 8.13% | 8.85% | 1.09x | ✅ |
| `int_to_big_endian[255]` | 1.4826918010866542e-06 | 9.13954078223826e-07 | 38.36% | 62.23% | 1.62x | ✅ |
| `int_to_big_endian[256]` | 1.4651082695946703e-06 | 8.971608884525212e-07 | 38.76% | 63.30% | 1.63x | ✅ |
| `int_to_big_endian[max]` | 1.787771815795354e-06 | 1.1217685079228687e-06 | 37.25% | 59.37% | 1.59x | ✅ |
| `int_to_big_endian[one]` | 1.4983276283678846e-06 | 8.90016922838739e-07 | 40.60% | 68.35% | 1.68x | ✅ |
| `int_to_big_endian[zero]` | 1.673838389716649e-06 | 1.017413893743807e-06 | 39.22% | 64.52% | 1.65x | ✅ |
