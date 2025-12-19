#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.317912218347341e-06 | 2.0734769556827955e-06 | 10.55% | 11.79% | 1.12x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.7675357964118834e-06 | 1.529380829556069e-06 | 13.47% | 15.57% | 1.16x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.9260010652296846e-06 | 1.6347444869462305e-06 | 15.12% | 17.82% | 1.18x | ✅ |
| `big_endian_to_int[one-byte]` | 1.9253289970260116e-06 | 1.6320897960275271e-06 | 15.23% | 17.97% | 1.18x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.9072324860184653e-06 | 1.6211920784803103e-06 | 15.00% | 17.64% | 1.18x | ✅ |
| `int_to_big_endian[255]` | 1.5512097776568479e-06 | 1.3259318735778742e-06 | 14.52% | 16.99% | 1.17x | ✅ |
| `int_to_big_endian[256]` | 1.5468022669593405e-06 | 1.3303140782385486e-06 | 14.00% | 16.27% | 1.16x | ✅ |
| `int_to_big_endian[max]` | 2.0689392248795202e-06 | 1.8852700303369138e-06 | 8.88% | 9.74% | 1.10x | ✅ |
| `int_to_big_endian[one]` | 1.5195036897568919e-06 | 1.327464326078232e-06 | 12.64% | 14.47% | 1.14x | ✅ |
| `int_to_big_endian[zero]` | 1.6558355865120905e-06 | 1.4161848259824894e-06 | 14.47% | 16.92% | 1.17x | ✅ |
