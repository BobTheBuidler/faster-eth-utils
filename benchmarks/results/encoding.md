#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1472063483018187e-06 | 1.989956211165236e-06 | 7.32% | 7.90% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6774825166931122e-06 | 1.46583643842337e-06 | 12.62% | 14.44% | 1.14x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.7935451571419698e-06 | 1.538292471786996e-06 | 14.23% | 16.59% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.7816411114110903e-06 | 1.5000174873800428e-06 | 15.81% | 18.77% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.774315932056884e-06 | 1.4853040041841559e-06 | 16.29% | 19.46% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.5727392341297835e-06 | 1.7700736335567609e-06 | -12.55% | -11.15% | 0.89x | ❌ |
| `int_to_big_endian[256]` | 1.5733567543240141e-06 | 1.7685680451001931e-06 | -12.41% | -11.04% | 0.89x | ❌ |
| `int_to_big_endian[max]` | 1.92388590241369e-06 | 2.114784122996722e-06 | -9.92% | -9.03% | 0.91x | ❌ |
| `int_to_big_endian[one]` | 1.5727488443728981e-06 | 1.775977462522863e-06 | -12.92% | -11.44% | 0.89x | ❌ |
| `int_to_big_endian[zero]` | 1.640843815443433e-06 | 1.8110431508495524e-06 | -10.37% | -9.40% | 0.91x | ❌ |
