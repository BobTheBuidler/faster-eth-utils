#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.362819576719325e-06 | 2.1302114655833375e-06 | 9.84% | 10.92% | 1.11x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7152240854134816e-06 | 1.5376858331727387e-06 | 10.35% | 11.55% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8762677408830156e-06 | 1.5580067688882455e-06 | 16.96% | 20.43% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8665011646673468e-06 | 1.5628471243939846e-06 | 16.27% | 19.43% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.8933071125707303e-06 | 1.5638303161210135e-06 | 17.40% | 21.07% | 1.21x | ✅ |
| `int_to_big_endian[255]` | 1.565090418721108e-06 | 1.460766821424785e-06 | 6.67% | 7.14% | 1.07x | ✅ |
| `int_to_big_endian[256]` | 1.5568673647403725e-06 | 1.4361581953498072e-06 | 7.75% | 8.41% | 1.08x | ✅ |
| `int_to_big_endian[max]` | 1.9418678790576495e-06 | 1.8690758523001505e-06 | 3.75% | 3.89% | 1.04x | ✅ |
| `int_to_big_endian[one]` | 1.5269303988694693e-06 | 1.4529139431830059e-06 | 4.85% | 5.09% | 1.05x | ✅ |
| `int_to_big_endian[zero]` | 1.653478207468532e-06 | 1.5583549084372493e-06 | 5.75% | 6.10% | 1.06x | ✅ |
