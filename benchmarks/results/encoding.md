#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.360569326078929e-06 | 2.0487353196800835e-06 | 13.21% | 15.22% | 1.15x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7593919548449167e-06 | 1.576827007929588e-06 | 10.38% | 11.58% | 1.12x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9339056811966256e-06 | 1.6503182999566262e-06 | 14.66% | 17.18% | 1.17x | ✅ |
| `big_endian_to_int[one-byte]` | 1.948088696220191e-06 | 1.6417042025038072e-06 | 15.73% | 18.66% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9543656200743577e-06 | 1.6455719127939802e-06 | 15.80% | 18.77% | 1.19x | ✅ |
| `int_to_big_endian[255]` | 1.564605259739675e-06 | 1.3502489528417705e-06 | 13.70% | 15.88% | 1.16x | ✅ |
| `int_to_big_endian[256]` | 1.5735520911276329e-06 | 1.351089465185613e-06 | 14.14% | 16.47% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 1.962202412340287e-06 | 1.674614830405586e-06 | 14.66% | 17.17% | 1.17x | ✅ |
| `int_to_big_endian[one]` | 1.5585894598283906e-06 | 1.3428218415324367e-06 | 13.84% | 16.07% | 1.16x | ✅ |
| `int_to_big_endian[zero]` | 1.6979484967757808e-06 | 1.4382085634132082e-06 | 15.30% | 18.06% | 1.18x | ✅ |
