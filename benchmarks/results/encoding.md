#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.107348106775504e-06 | 1.8313218424244473e-06 | 13.10% | 15.07% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5729912358010614e-06 | 1.4198636540198337e-06 | 9.73% | 10.78% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7370703585967795e-06 | 1.468624179379335e-06 | 15.45% | 18.28% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8230542622967627e-06 | 1.4678692053541423e-06 | 19.48% | 24.20% | 1.24x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7408647525860756e-06 | 1.4768224365857816e-06 | 15.17% | 17.88% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.577391753364838e-06 | 1.310611305432145e-06 | 16.91% | 20.36% | 1.20x | ✅ |
| `int_to_big_endian[256]` | 1.5348873566067661e-06 | 1.3512498583642255e-06 | 11.96% | 13.59% | 1.14x | ✅ |
| `int_to_big_endian[max]` | 1.8926641608476973e-06 | 1.6340077754864246e-06 | 13.67% | 15.83% | 1.16x | ✅ |
| `int_to_big_endian[one]` | 1.7002612415194654e-06 | 1.2967561500804728e-06 | 23.73% | 31.12% | 1.31x | ✅ |
| `int_to_big_endian[zero]` | 1.8414245435519047e-06 | 1.42678003414169e-06 | 22.52% | 29.06% | 1.29x | ✅ |
