#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.1697380047869766e-06 | 1.877525094278169e-06 | 13.47% | 15.56% | 1.16x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.6920992913003515e-06 | 1.4332309103158304e-06 | 15.30% | 18.06% | 1.18x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.792281579525525e-06 | 1.4946690826709267e-06 | 16.61% | 19.91% | 1.20x | ✅ |
| `big_endian_to_int[one-byte]` | 1.799174843178058e-06 | 1.5065403260816778e-06 | 16.26% | 19.42% | 1.19x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.770021298281819e-06 | 1.5210866212982325e-06 | 14.06% | 16.37% | 1.16x | ✅ |
| `int_to_big_endian[255]` | 1.5820781802768257e-06 | 1.7449713546699716e-06 | -10.30% | -9.34% | 0.91x | ❌ |
| `int_to_big_endian[256]` | 1.6307462286692995e-06 | 1.7370052526095042e-06 | -6.52% | -6.12% | 0.94x | ❌ |
| `int_to_big_endian[max]` | 1.9409053051745464e-06 | 2.225779753703085e-06 | -14.68% | -12.80% | 0.87x | ❌ |
| `int_to_big_endian[one]` | 1.5933015604589491e-06 | 1.7346904321672118e-06 | -8.87% | -8.15% | 0.92x | ❌ |
| `int_to_big_endian[zero]` | 1.6835349533626922e-06 | 1.8476566597235511e-06 | -9.75% | -8.88% | 0.91x | ❌ |
