#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1810558989177577e-06 | 1.8939899356090025e-06 | 13.16% | 15.16% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6991669487559648e-06 | 1.5237560436357158e-06 | 10.32% | 11.51% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7919836610861025e-06 | 1.5843674003523694e-06 | 11.59% | 13.10% | 1.13x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7895645243916823e-06 | 1.5663258953229059e-06 | 12.47% | 14.25% | 1.14x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.79441515494626e-06 | 1.5739154485330768e-06 | 12.29% | 14.01% | 1.14x | ✅ |
| `int_to_big_endian[255]` | 1.5780404011763543e-06 | 1.7705476093181748e-06 | -12.20% | -10.87% | 0.89x | ❌ |
| `int_to_big_endian[256]` | 1.5872393120119331e-06 | 1.7547425467136296e-06 | -10.55% | -9.55% | 0.90x | ❌ |
| `int_to_big_endian[max]` | 1.9472145855791503e-06 | 2.1508803286816796e-06 | -10.46% | -9.47% | 0.91x | ❌ |
| `int_to_big_endian[one]` | 1.5781396571958467e-06 | 1.7739709633285013e-06 | -12.41% | -11.04% | 0.89x | ❌ |
| `int_to_big_endian[zero]` | 1.6591440522576967e-06 | 1.8245045841741944e-06 | -9.97% | -9.06% | 0.91x | ❌ |
