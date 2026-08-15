#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.410802292260913e-06 | 2.1194417297645184e-06 | 12.09% | 13.75% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7633205056554956e-06 | 1.6125704401469835e-06 | 8.55% | 9.35% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.910106109473812e-06 | 1.8129670208824712e-06 | 5.09% | 5.36% | 1.05x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9456547715058877e-06 | 1.9266003823096687e-06 | 0.98% | 0.99% | 1.01x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.924360555814638e-06 | 1.8873703580353494e-06 | 1.92% | 1.96% | 1.02x | ✅ |
| `int_to_big_endian[255]` | 1.6624460342423697e-06 | 9.560085027933518e-07 | 42.49% | 73.89% | 1.74x | ✅ |
| `int_to_big_endian[256]` | 1.601033980730639e-06 | 9.539904090244074e-07 | 40.41% | 67.82% | 1.68x | ✅ |
| `int_to_big_endian[max]` | 2.0367997387289233e-06 | 1.1953631716398554e-06 | 41.31% | 70.39% | 1.70x | ✅ |
| `int_to_big_endian[one]` | 1.6557192910110575e-06 | 9.570456744309356e-07 | 42.20% | 73.00% | 1.73x | ✅ |
| `int_to_big_endian[zero]` | 1.775240572539957e-06 | 1.0886919127681796e-06 | 38.67% | 63.06% | 1.63x | ✅ |
