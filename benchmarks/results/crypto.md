#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/to-bytes/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.132143925107203e-05 | 1.6680964459982377e-05 | 46.74% | 87.77% | 1.88x | ✅ |
| `keccak[bytes]` | 3.359189020131164e-05 | 1.868229464349351e-05 | 44.38% | 79.81% | 1.80x | ✅ |
| `keccak[hexstr]` | 4.1738611919660057e-05 | 2.1111733824247405e-05 | 49.42% | 97.70% | 1.98x | ✅ |
| `keccak[int]` | 9.273157965875e-05 | 2.9088071927046686e-05 | 68.63% | 218.80% | 3.19x | ✅ |
| `keccak[text]` | 3.558418078350842e-05 | 1.94271926254234e-05 | 45.40% | 83.17% | 1.83x | ✅ |
