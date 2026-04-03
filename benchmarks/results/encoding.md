#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.3838982029062187e-06 | 2.142508864521936e-06 | 10.13% | 11.27% | 1.11x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7233963111710718e-06 | 1.5498008379232527e-06 | 10.07% | 11.20% | 1.11x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.8889865224899324e-06 | 1.6421517325077062e-06 | 13.07% | 15.03% | 1.15x | ✅ |
| `big_endian_to_int[one-byte]` | 1.872221763752325e-06 | 1.6171634682930014e-06 | 13.62% | 15.77% | 1.16x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.8969612765476232e-06 | 1.6412008406623731e-06 | 13.48% | 15.58% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.5695664987382654e-06 | 9.277365279082861e-07 | 40.89% | 69.18% | 1.69x | ✅ |
| `int_to_big_endian[256]` | 1.5725862588987743e-06 | 9.074146087120754e-07 | 42.30% | 73.30% | 1.73x | ✅ |
| `int_to_big_endian[max]` | 1.970627197693996e-06 | 1.1392573346235118e-06 | 42.19% | 72.97% | 1.73x | ✅ |
| `int_to_big_endian[one]` | 1.5874922566582495e-06 | 9.127490006359726e-07 | 42.50% | 73.92% | 1.74x | ✅ |
| `int_to_big_endian[zero]` | 1.6965246832105894e-06 | 1.039368740577307e-06 | 38.74% | 63.23% | 1.63x | ✅ |
