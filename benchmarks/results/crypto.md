#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.697974932231106e-05 | 6.99320796200857e-05 | 19.60% | 24.38% | 1.24x | ✅ |
| `keccak[bytes]` | 8.838658023895515e-05 | 7.28123867644375e-05 | 17.62% | 21.39% | 1.21x | ✅ |
| `keccak[hexstr]` | 0.00010194088496336904 | 7.472539856245871e-05 | 26.70% | 36.42% | 1.36x | ✅ |
| `keccak[int]` | 0.00015682771136043053 | 8.402137286006582e-05 | 46.42% | 86.65% | 1.87x | ✅ |
| `keccak[text]` | 9.161905664505241e-05 | 7.300816195457425e-05 | 20.31% | 25.49% | 1.25x | ✅ |
