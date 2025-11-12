#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1986828637685524e-06 | 1.8806329447268935e-06 | 14.47% | 16.91% | 1.17x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6881164083842247e-06 | 1.4796678427897786e-06 | 12.35% | 14.09% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7746217850528477e-06 | 1.4987706634590441e-06 | 15.54% | 18.41% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.780717417500716e-06 | 1.4974345394220095e-06 | 15.91% | 18.92% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7751080168005942e-06 | 1.4932473306489724e-06 | 15.88% | 18.88% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5856790634972112e-06 | 1.7475358423396706e-06 | -10.21% | -9.26% | 0.91x | ❌ |
| `int_to_big_endian[256]` | 1.6904198082655343e-06 | 1.7778586440139378e-06 | -5.17% | -4.92% | 0.95x | ❌ |
| `int_to_big_endian[max]` | 2.080206310768759e-06 | 2.0032085578577273e-06 | 3.70% | 3.84% | 1.04x | ✅ |
| `int_to_big_endian[one]` | 1.6868867268195537e-06 | 1.7003854227836477e-06 | -0.80% | -0.79% | 0.99x | ❌ |
| `int_to_big_endian[zero]` | 1.693718489867828e-06 | 1.7594369540409676e-06 | -3.88% | -3.74% | 0.96x | ❌ |
