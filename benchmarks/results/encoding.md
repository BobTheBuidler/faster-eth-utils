#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.0887470315025735e-06 | 2.079503886346766e-06 | 0.44% | 0.44% | 1.00x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.5672276670176093e-06 | 1.413755926661576e-06 | 9.79% | 10.86% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7229000975579271e-06 | 1.4753752735864302e-06 | 14.37% | 16.78% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.723554076349068e-06 | 1.4716936242840042e-06 | 14.61% | 17.11% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.73265539770282e-06 | 1.4921283096799764e-06 | 13.88% | 16.12% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.472995366491046e-06 | 1.278409210013542e-06 | 13.21% | 15.22% | 1.15x | ✅ |
| `int_to_big_endian[256]` | 1.4790235314918467e-06 | 1.2767928229145751e-06 | 13.67% | 15.84% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.8393122290876134e-06 | 1.7034447179517395e-06 | 7.39% | 7.98% | 1.08x | ✅ |
| `int_to_big_endian[one]` | 1.4630428138506953e-06 | 1.2724664386780244e-06 | 13.03% | 14.98% | 1.15x | ✅ |
| `int_to_big_endian[zero]` | 1.5652908605413525e-06 | 1.3403805167320209e-06 | 14.37% | 16.78% | 1.17x | ✅ |
