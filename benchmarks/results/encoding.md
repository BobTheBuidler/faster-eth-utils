#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3729484740952637e-06 | 2.2182420706291284e-06 | 6.52% | 6.97% | 1.07x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.714614318748865e-06 | 1.525148344542265e-06 | 11.05% | 12.42% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8811250757607348e-06 | 1.6376381412285108e-06 | 12.94% | 14.87% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8461462681896635e-06 | 1.7257989207998112e-06 | 6.52% | 6.97% | 1.07x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.887095728147499e-06 | 1.6397179008522073e-06 | 13.11% | 15.09% | 1.15x | ✅ |
| `int_to_big_endian[255]` | 1.5965415554336817e-06 | 9.054594498294664e-07 | 43.29% | 76.32% | 1.76x | ✅ |
| `int_to_big_endian[256]` | 1.6325661117875967e-06 | 9.061472127693862e-07 | 44.50% | 80.17% | 1.80x | ✅ |
| `int_to_big_endian[max]` | 1.9708439576702825e-06 | 1.1434115631347204e-06 | 41.98% | 72.37% | 1.72x | ✅ |
| `int_to_big_endian[one]` | 1.5568240603571147e-06 | 9.261662444484808e-07 | 40.51% | 68.09% | 1.68x | ✅ |
| `int_to_big_endian[zero]` | 1.7050348100086891e-06 | 1.0226212626665448e-06 | 40.02% | 66.73% | 1.67x | ✅ |
