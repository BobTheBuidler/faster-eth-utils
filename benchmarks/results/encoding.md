#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.4009310162397895e-06 | 2.1148139197599794e-06 | 11.92% | 13.53% | 1.14x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7568959200073403e-06 | 1.540621862636362e-06 | 12.31% | 14.04% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.89135844511716e-06 | 1.5799469373165796e-06 | 16.46% | 19.71% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.901842725905895e-06 | 1.567031178463089e-06 | 17.60% | 21.37% | 1.21x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.910496267349812e-06 | 1.559702397625839e-06 | 18.36% | 22.49% | 1.22x | ✅ |
| `int_to_big_endian[255]` | 1.5863640414375777e-06 | 1.447621019091114e-06 | 8.75% | 9.58% | 1.10x | ✅ |
| `int_to_big_endian[256]` | 1.5681076846807866e-06 | 1.4322010734475942e-06 | 8.67% | 9.49% | 1.09x | ✅ |
| `int_to_big_endian[max]` | 1.956561510302008e-06 | 1.8486385647742848e-06 | 5.52% | 5.84% | 1.06x | ✅ |
| `int_to_big_endian[one]` | 1.583346184925769e-06 | 1.4511595985336635e-06 | 8.35% | 9.11% | 1.09x | ✅ |
| `int_to_big_endian[zero]` | 1.7096557123929032e-06 | 1.5503589684730305e-06 | 9.32% | 10.27% | 1.10x | ✅ |
