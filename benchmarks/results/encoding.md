#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.184539944192962e-06 | 1.885011618932191e-06 | 13.71% | 15.89% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.664423617271131e-06 | 1.5042028807885705e-06 | 9.63% | 10.65% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7974780186194706e-06 | 1.5454065979078382e-06 | 14.02% | 16.31% | 1.16x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8006366639434374e-06 | 1.5605500378085352e-06 | 13.33% | 15.38% | 1.15x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7945105135957192e-06 | 1.555251404996577e-06 | 13.33% | 15.38% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.6170644988939957e-06 | 1.7336316996396407e-06 | -7.21% | -6.72% | 0.93x | ❌ |
| `int_to_big_endian[256]` | 1.572922987453807e-06 | 1.8118012613226245e-06 | -15.19% | -13.18% | 0.87x | ❌ |
| `int_to_big_endian[max]` | 1.9310099130777857e-06 | 2.1158937213563636e-06 | -9.57% | -8.74% | 0.91x | ❌ |
| `int_to_big_endian[one]` | 1.6016531387407262e-06 | 1.7423973122690884e-06 | -8.79% | -8.08% | 0.92x | ❌ |
| `int_to_big_endian[zero]` | 1.6091690552941782e-06 | 1.7895574454589278e-06 | -11.21% | -10.08% | 0.90x | ❌ |
