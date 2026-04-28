#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3799275095378177e-06 | 2.201779362917456e-06 | 7.49% | 8.09% | 1.08x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6424511305977155e-06 | 1.5949596790529397e-06 | 2.89% | 2.98% | 1.03x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8048746923016373e-06 | 1.6351128247438776e-06 | 9.41% | 10.38% | 1.10x | ✅ |
| `big_endian_to_int[one-byte]` | 1.8028567535592068e-06 | 1.665111633698131e-06 | 7.64% | 8.27% | 1.08x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.7960907257842409e-06 | 1.654257172438352e-06 | 7.90% | 8.57% | 1.09x | ✅ |
| `int_to_big_endian[255]` | 1.6208297486386532e-06 | 9.766980482940306e-07 | 39.74% | 65.95% | 1.66x | ✅ |
| `int_to_big_endian[256]` | 1.5816577268045818e-06 | 9.35220807779892e-07 | 40.87% | 69.12% | 1.69x | ✅ |
| `int_to_big_endian[max]` | 2.0601533943563975e-06 | 1.2255696596958957e-06 | 40.51% | 68.10% | 1.68x | ✅ |
| `int_to_big_endian[one]` | 1.6151982379195602e-06 | 9.863902382521712e-07 | 38.93% | 63.75% | 1.64x | ✅ |
| `int_to_big_endian[zero]` | 1.666730093061786e-06 | 1.0931014077484575e-06 | 34.42% | 52.48% | 1.52x | ✅ |
