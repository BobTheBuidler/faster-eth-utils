#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4160372059288407e-06 | 2.2327046390377135e-06 | 7.59% | 8.21% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.8440486520833522e-06 | 1.7377284081679114e-06 | 5.77% | 6.12% | 1.06x | ✅ |
| `big_endian_to_int[ff-byte]` | 2.0391899543129923e-06 | 1.8038123097213664e-06 | 11.54% | 13.05% | 1.13x | ✅ |
| `big_endian_to_int[one-byte]` | 2.037140955795384e-06 | 1.8045472988744886e-06 | 11.42% | 12.89% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 2.06821577649943e-06 | 1.9078844413315285e-06 | 7.75% | 8.40% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.4685644335663458e-06 | 1.7775099535896462e-06 | -21.04% | -17.38% | 0.83x | ❌ |
| `int_to_big_endian[256]` | 1.4739854250413561e-06 | 1.6933338596663084e-06 | -14.88% | -12.95% | 0.87x | ❌ |
| `int_to_big_endian[max]` | 1.952171988614044e-06 | 2.043564650432676e-06 | -4.68% | -4.47% | 0.96x | ❌ |
| `int_to_big_endian[one]` | 1.4996059545764974e-06 | 1.692719138049044e-06 | -12.88% | -11.41% | 0.89x | ❌ |
| `int_to_big_endian[zero]` | 1.6186234018793728e-06 | 1.7306931567495657e-06 | -6.92% | -6.48% | 0.94x | ❌ |
