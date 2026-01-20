#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.381602215404207e-06 | 2.222703819842451e-06 | 6.67% | 7.15% | 1.07x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7632304886794153e-06 | 1.6652657839170858e-06 | 5.56% | 5.88% | 1.06x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9463325707701555e-06 | 1.7221669095984397e-06 | 11.52% | 13.02% | 1.13x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9559864648943732e-06 | 1.7141292783246196e-06 | 12.36% | 14.11% | 1.14x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.966014397710138e-06 | 1.7034986947988823e-06 | 13.35% | 15.41% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5616857131705515e-06 | 1.4029537316923528e-06 | 10.16% | 11.31% | 1.11x | ✅ |
| `int_to_big_endian[256]` | 1.5566799181306096e-06 | 1.3492469626981881e-06 | 13.33% | 15.37% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.9047127917247422e-06 | 1.7959186700814994e-06 | 5.71% | 6.06% | 1.06x | ✅ |
| `int_to_big_endian[one]` | 1.5865769161152034e-06 | 1.3502875677803938e-06 | 14.89% | 17.50% | 1.17x | ✅ |
| `int_to_big_endian[zero]` | 1.6885228174762168e-06 | 1.450841722545529e-06 | 14.08% | 16.38% | 1.16x | ✅ |
