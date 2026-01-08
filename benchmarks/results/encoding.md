#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/diagnose-test-failures-in-pr/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.36861596412438e-06 | 2.1802933382430268e-06 | 7.95% | 8.64% | 1.09x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7837766116433962e-06 | 1.6715690745753726e-06 | 6.29% | 6.71% | 1.07x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.937963097662712e-06 | 1.6880758365505723e-06 | 12.89% | 14.80% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.94548986566932e-06 | 1.6933650343796895e-06 | 12.96% | 14.89% | 1.15x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9657857235466605e-06 | 1.6846425624780605e-06 | 14.30% | 16.69% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.565113142024551e-06 | 1.4245185031134202e-06 | 8.98% | 9.87% | 1.10x | ✅ |
| `int_to_big_endian[256]` | 1.5628173282821535e-06 | 1.3921916179815839e-06 | 10.92% | 12.26% | 1.12x | ✅ |
| `int_to_big_endian[max]` | 1.9524231213917837e-06 | 1.8367291245308244e-06 | 5.93% | 6.30% | 1.06x | ✅ |
| `int_to_big_endian[one]` | 1.6716345299453949e-06 | 1.3994901588898314e-06 | 16.28% | 19.45% | 1.19x | ✅ |
| `int_to_big_endian[zero]` | 1.6805843262732079e-06 | 1.4700488404366493e-06 | 12.53% | 14.32% | 1.14x | ✅ |
