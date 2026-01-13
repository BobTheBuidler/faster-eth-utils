#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3501654377814195e-06 | 2.0361964416263226e-06 | 13.36% | 15.42% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.772642468674036e-06 | 1.5553030767789187e-06 | 12.26% | 13.97% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.945521355992475e-06 | 1.6387838103354609e-06 | 15.77% | 18.72% | 1.19x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9606111879545476e-06 | 1.6339192359858224e-06 | 16.66% | 19.99% | 1.20x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9293647953341846e-06 | 1.6429072797036676e-06 | 14.85% | 17.44% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.5447466889529086e-06 | 1.3387559281669398e-06 | 13.33% | 15.39% | 1.15x | ✅ |
| `int_to_big_endian[256]` | 1.5471919656438968e-06 | 1.3356514142556383e-06 | 13.67% | 15.84% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.932784952968523e-06 | 1.6610694465129962e-06 | 14.06% | 16.36% | 1.16x | ✅ |
| `int_to_big_endian[one]` | 1.563985535214664e-06 | 1.3297341906392796e-06 | 14.98% | 17.62% | 1.18x | ✅ |
| `int_to_big_endian[zero]` | 1.6850533864880262e-06 | 1.419174443036828e-06 | 15.78% | 18.73% | 1.19x | ✅ |
