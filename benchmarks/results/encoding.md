#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3298590085191603e-06 | 2.084462532984638e-06 | 10.53% | 11.77% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7646341106357133e-06 | 1.5507511028021469e-06 | 12.12% | 13.79% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.925797874322415e-06 | 1.6398874590129216e-06 | 14.85% | 17.43% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9365856804128718e-06 | 1.6399850614762867e-06 | 15.32% | 18.09% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9246996350218725e-06 | 1.6392031842527295e-06 | 14.83% | 17.42% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.5415058819341863e-06 | 1.3331309390920215e-06 | 13.52% | 15.63% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5419564088912187e-06 | 1.341075988692154e-06 | 13.03% | 14.98% | 1.15x | ✅ |
| `int_to_big_endian[max]` | 1.938194448545261e-06 | 1.656918443785114e-06 | 14.51% | 16.98% | 1.17x | ✅ |
| `int_to_big_endian[one]` | 1.5607869780942431e-06 | 1.3262248831140524e-06 | 15.03% | 17.69% | 1.18x | ✅ |
| `int_to_big_endian[zero]` | 1.670208219913122e-06 | 1.4213805533987828e-06 | 14.90% | 17.51% | 1.18x | ✅ |
