#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3459145070189207e-06 | 2.048446148476256e-06 | 12.68% | 14.52% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7804862833051418e-06 | 1.4654582774088846e-06 | 17.69% | 21.50% | 1.21x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9433973251176955e-06 | 1.6248369831192698e-06 | 16.39% | 19.61% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9205664745111675e-06 | 1.6278776554428746e-06 | 15.24% | 17.98% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.927314239355525e-06 | 1.6413388373135936e-06 | 14.84% | 17.42% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.574562374086471e-06 | 1.3297883940287267e-06 | 15.55% | 18.41% | 1.18x | ✅ |
| `int_to_big_endian[256]` | 1.5602426869139657e-06 | 1.3397456429915595e-06 | 14.13% | 16.46% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.93227425438835e-06 | 1.6611704481220183e-06 | 14.03% | 16.32% | 1.16x | ✅ |
| `int_to_big_endian[one]` | 1.5378372907375182e-06 | 1.3327602153688225e-06 | 13.34% | 15.39% | 1.15x | ✅ |
| `int_to_big_endian[zero]` | 1.6518126079551464e-06 | 1.3337098987675973e-06 | 19.26% | 23.85% | 1.24x | ✅ |
