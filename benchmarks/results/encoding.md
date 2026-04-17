#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.331784667956381e-06 | 2.0814716097412908e-06 | 10.73% | 12.03% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.627041223857738e-06 | 1.589857880923085e-06 | 2.29% | 2.34% | 1.02x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7832607451271053e-06 | 1.6392365967288654e-06 | 8.08% | 8.79% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7760425774517337e-06 | 1.659487984968796e-06 | 6.56% | 7.02% | 1.07x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7675081277328006e-06 | 1.6372852906009908e-06 | 7.37% | 7.95% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.6192013430340099e-06 | 9.793006303563227e-07 | 39.52% | 65.34% | 1.65x | ✅ |
| `int_to_big_endian[256]` | 1.564817166876567e-06 | 9.444757352963011e-07 | 39.64% | 65.68% | 1.66x | ✅ |
| `int_to_big_endian[max]` | 2.077027779802736e-06 | 1.253184297340242e-06 | 39.66% | 65.74% | 1.66x | ✅ |
| `int_to_big_endian[one]` | 1.5943010192070285e-06 | 9.796539383784337e-07 | 38.55% | 62.74% | 1.63x | ✅ |
| `int_to_big_endian[zero]` | 1.6887579769593968e-06 | 1.0731103832850954e-06 | 36.46% | 57.37% | 1.57x | ✅ |
