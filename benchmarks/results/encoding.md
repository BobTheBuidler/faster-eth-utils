#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1787850125448506e-06 | 2.0475966828212087e-06 | 6.02% | 6.41% | 1.06x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6654170445119918e-06 | 1.47509066568849e-06 | 11.43% | 12.90% | 1.13x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7867241943780722e-06 | 1.5932082072740461e-06 | 10.83% | 12.15% | 1.12x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7892065033452167e-06 | 1.5797151319619821e-06 | 11.71% | 13.26% | 1.13x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7876064419220803e-06 | 1.5596643660363032e-06 | 12.75% | 14.61% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5462159688530124e-06 | 1.7876962925190001e-06 | -15.62% | -13.51% | 0.86x | ❌ |
| `int_to_big_endian[256]` | 1.552594247211699e-06 | 1.7814469078665465e-06 | -14.74% | -12.85% | 0.87x | ❌ |
| `int_to_big_endian[max]` | 1.9056769087480575e-06 | 2.1321566364229845e-06 | -11.88% | -10.62% | 0.89x | ❌ |
| `int_to_big_endian[one]` | 1.5874855619923875e-06 | 1.7800463247876439e-06 | -12.13% | -10.82% | 0.89x | ❌ |
| `int_to_big_endian[zero]` | 1.6360143206720022e-06 | 1.8371315328714889e-06 | -12.29% | -10.95% | 0.89x | ❌ |
