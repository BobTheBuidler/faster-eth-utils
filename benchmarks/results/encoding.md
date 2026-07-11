#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1113907353129996e-06 | 2.1543417911232996e-06 | -2.03% | -1.99% | 0.98x | ❌ |
| `big_endian_to_int[empty-bytes]` | 1.5450243769133357e-06 | 1.592542911710216e-06 | -3.08% | -2.98% | 0.97x | ❌ |
| `big_endian_to_int[ff-byte]` | 1.7750314096143664e-06 | 1.6565655549350116e-06 | 6.67% | 7.15% | 1.07x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7971545554691043e-06 | 1.6423565030227494e-06 | 8.61% | 9.43% | 1.09x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7807645500696383e-06 | 1.6481866442968607e-06 | 7.44% | 8.04% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.4783177511845096e-06 | 8.961154353877405e-07 | 39.38% | 64.97% | 1.65x | ✅ |
| `int_to_big_endian[256]` | 1.524407082730941e-06 | 8.915273868822781e-07 | 41.52% | 70.99% | 1.71x | ✅ |
| `int_to_big_endian[max]` | 1.839243449739632e-06 | 1.092627617756521e-06 | 40.59% | 68.33% | 1.68x | ✅ |
| `int_to_big_endian[one]` | 1.4807228381342743e-06 | 9.269682424031878e-07 | 37.40% | 59.74% | 1.60x | ✅ |
| `int_to_big_endian[zero]` | 1.6153562712291733e-06 | 1.0357151574822317e-06 | 35.88% | 55.97% | 1.56x | ✅ |
