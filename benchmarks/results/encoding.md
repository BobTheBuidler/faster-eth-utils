#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4295217376544034e-06 | 2.2323787642445118e-06 | 8.11% | 8.83% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7530630114134382e-06 | 1.644305061491563e-06 | 6.20% | 6.61% | 1.07x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.990518135029482e-06 | 1.7925580806396723e-06 | 9.95% | 11.04% | 1.11x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9882382299940143e-06 | 1.8064189311825927e-06 | 9.14% | 10.07% | 1.10x | ✅ |
| `big_endian_to_int[two-bytes]` | 2.011005980983914e-06 | 1.7880034479006546e-06 | 11.09% | 12.47% | 1.12x | ✅ |
| `int_to_big_endian[255]` | 1.5291983837266436e-06 | 1.5443826906615036e-06 | -0.99% | -0.98% | 0.99x | ❌ |
| `int_to_big_endian[256]` | 1.5360267939371012e-06 | 1.5290503262696603e-06 | 0.45% | 0.46% | 1.00x | ✅ |
| `int_to_big_endian[max]` | 1.9418875338916487e-06 | 2.028400778816613e-06 | -4.46% | -4.27% | 0.96x | ❌ |
| `int_to_big_endian[one]` | 1.5448604328811824e-06 | 1.5338513859760348e-06 | 0.71% | 0.72% | 1.01x | ✅ |
| `int_to_big_endian[zero]` | 1.600882691727825e-06 | 1.615811850142958e-06 | -0.93% | -0.92% | 0.99x | ❌ |
