#### [faster_eth_utils.encoding](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/encoding.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_encoding_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `big_endian_to_int[32-ff-bytes]` | 2.5464612100510716e-06 | 2.2469327546249956e-06 | 11.76% | 13.33% | 1.13x | ✅ |
| `big_endian_to_int[empty-bytes]` | 1.8630837430529864e-06 | 1.7117991688019115e-06 | 8.12% | 8.84% | 1.09x | ✅ |
| `big_endian_to_int[ff-byte]` | 1.945660448154064e-06 | 1.7699595788872159e-06 | 9.03% | 9.93% | 1.10x | ✅ |
| `big_endian_to_int[one-byte]` | 1.920796808056447e-06 | 1.7404234539500202e-06 | 9.39% | 10.36% | 1.10x | ✅ |
| `big_endian_to_int[two-bytes]` | 1.903191096309539e-06 | 1.7561587622296335e-06 | 7.73% | 8.37% | 1.08x | ✅ |
| `int_to_big_endian[255]` | 1.7415307769302019e-06 | 1.0821921244189518e-06 | 37.86% | 60.93% | 1.61x | ✅ |
| `int_to_big_endian[256]` | 1.7224475164175839e-06 | 1.04818822161279e-06 | 39.15% | 64.33% | 1.64x | ✅ |
| `int_to_big_endian[max]` | 2.2682737404384014e-06 | 1.3309483380004077e-06 | 41.32% | 70.43% | 1.70x | ✅ |
| `int_to_big_endian[one]` | 1.7223331719917214e-06 | 1.0731701474805944e-06 | 37.69% | 60.49% | 1.60x | ✅ |
| `int_to_big_endian[zero]` | 1.7977379905759184e-06 | 1.1862357050691187e-06 | 34.02% | 51.55% | 1.52x | ✅ |
