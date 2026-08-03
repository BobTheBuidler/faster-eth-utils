#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3177280031599155e-06 | 2.048628858274246e-06 | 11.61% | 13.14% | 1.13x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7725932995063456e-06 | 1.6206321163531304e-06 | 8.57% | 9.38% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9621977297262475e-06 | 1.7970766574053786e-06 | 8.42% | 9.19% | 1.09x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9982378752415916e-06 | 1.8046885382371542e-06 | 9.69% | 10.72% | 1.11x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9114214345853833e-06 | 1.7738873941847096e-06 | 7.20% | 7.75% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.60899690488332e-06 | 9.50396514635245e-07 | 40.93% | 69.30% | 1.69x | ✅ |
| `int_to_big_endian[256]` | 1.6013164311196752e-06 | 9.431382318942796e-07 | 41.10% | 69.79% | 1.70x | ✅ |
| `int_to_big_endian[max]` | 2.022046423443516e-06 | 1.1799079880859682e-06 | 41.65% | 71.37% | 1.71x | ✅ |
| `int_to_big_endian[one]` | 1.6074507086169218e-06 | 9.395333355083489e-07 | 41.55% | 71.09% | 1.71x | ✅ |
| `int_to_big_endian[zero]` | 1.6741970031965252e-06 | 1.1201494928379287e-06 | 33.09% | 49.46% | 1.49x | ✅ |
