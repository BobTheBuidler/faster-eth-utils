#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4225961566844195e-06 | 2.137195365726402e-06 | 11.78% | 13.35% | 1.13x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.9304705328575406e-06 | 1.5773768827198513e-06 | 18.29% | 22.38% | 1.22x | ✅ |
| `big_endian_to_int[ff-byte]` | 2.0026504438962644e-06 | 1.6433782355347903e-06 | 17.94% | 21.86% | 1.22x | ✅ |
| `big_endian_to_int[one-byte]` | 1.996918963458176e-06 | 1.6494606411183262e-06 | 17.40% | 21.06% | 1.21x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9950791057123798e-06 | 1.644963255856496e-06 | 17.55% | 21.28% | 1.21x | ✅ |
| `int_to_big_endian[255]` | 1.574203525051813e-06 | 1.3368472076269934e-06 | 15.08% | 17.75% | 1.18x | ✅ |
| `int_to_big_endian[256]` | 1.5771241235764888e-06 | 1.3327912257025166e-06 | 15.49% | 18.33% | 1.18x | ✅ |
| `int_to_big_endian[max]` | 2.0187704730264617e-06 | 1.6472958564247393e-06 | 18.40% | 22.55% | 1.23x | ✅ |
| `int_to_big_endian[one]` | 1.5939926404914823e-06 | 1.3290968346149545e-06 | 16.62% | 19.93% | 1.20x | ✅ |
| `int_to_big_endian[zero]` | 1.6914567901113736e-06 | 1.4433917194645505e-06 | 14.67% | 17.19% | 1.17x | ✅ |
