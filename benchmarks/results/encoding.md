#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3042515258583416e-06 | 2.1382435849741703e-06 | 7.20% | 7.76% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7539215711872242e-06 | 1.5130519320107712e-06 | 13.73% | 15.92% | 1.16x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.930358424234298e-06 | 1.6506943483100365e-06 | 14.49% | 16.94% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.916683866694854e-06 | 1.6442456079401289e-06 | 14.21% | 16.57% | 1.17x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9196884278593938e-06 | 1.6352291471249814e-06 | 14.82% | 17.40% | 1.17x | ✅ |
| `int_to_big_endian[255]` | 1.5452723033410477e-06 | 1.3373460779098727e-06 | 13.46% | 15.55% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5366974810860176e-06 | 1.3256394029597284e-06 | 13.73% | 15.92% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.941270442444825e-06 | 1.7421993393033406e-06 | 10.25% | 11.43% | 1.11x | ✅ |
| `int_to_big_endian[one]` | 1.5381545104577179e-06 | 1.3304241412657994e-06 | 13.51% | 15.61% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6786797805809096e-06 | 1.431924258804266e-06 | 14.70% | 17.23% | 1.17x | ✅ |
