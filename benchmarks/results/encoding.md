#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3396262823733444e-06 | 2.041778848139938e-06 | 12.73% | 14.59% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7685888748748772e-06 | 1.4933808151570737e-06 | 15.56% | 18.43% | 1.18x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.881129402948374e-06 | 1.655079219328217e-06 | 12.02% | 13.66% | 1.14x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8146695975575657e-06 | 1.637100498771145e-06 | 9.79% | 10.85% | 1.11x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.861776214198927e-06 | 1.6425217038404528e-06 | 11.78% | 13.35% | 1.13x | ✅ |
| `int_to_big_endian[255]` | 1.495569545211768e-06 | 1.2740575242280027e-06 | 14.81% | 17.39% | 1.17x | ✅ |
| `int_to_big_endian[256]` | 1.5197818998299383e-06 | 1.3082828135653505e-06 | 13.92% | 16.17% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.8702829555076218e-06 | 1.613661655436672e-06 | 13.72% | 15.90% | 1.16x | ✅ |
| `int_to_big_endian[one]` | 1.5203592227089136e-06 | 1.2764765123417294e-06 | 16.04% | 19.11% | 1.19x | ✅ |
| `int_to_big_endian[zero]` | 1.690565008892259e-06 | 1.3824969807217137e-06 | 18.22% | 22.28% | 1.22x | ✅ |
