#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.139184852615336e-06 | 1.863077380599953e-06 | 12.91% | 14.82% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.67717711324202e-06 | 1.4375779967560909e-06 | 14.29% | 16.67% | 1.17x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7837844106393853e-06 | 1.4828641737685477e-06 | 16.87% | 20.29% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.779746637043327e-06 | 1.482258897489527e-06 | 16.72% | 20.07% | 1.20x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7699790693021872e-06 | 1.4821984727089354e-06 | 16.26% | 19.42% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5705484463058302e-06 | 1.3417471936539753e-06 | 14.57% | 17.05% | 1.17x | ✅ |
| `int_to_big_endian[256]` | 1.5456346665513577e-06 | 1.3522211551515913e-06 | 12.51% | 14.30% | 1.14x | ✅ |
| `int_to_big_endian[max]` | 1.888810626660962e-06 | 1.7818184946998953e-06 | 5.66% | 6.00% | 1.06x | ✅ |
| `int_to_big_endian[one]` | 1.5417482015026878e-06 | 1.3317654591157041e-06 | 13.62% | 15.77% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6474455174936408e-06 | 1.4254365015844166e-06 | 13.48% | 15.57% | 1.16x | ✅ |
