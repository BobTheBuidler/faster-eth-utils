#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.137653040111617e-05 | 1.6778321185234944e-05 | 46.53% | 87.01% | 1.87x | ✅ |
| `keccak[bytes]` | 3.2929322594544545e-05 | 1.8676040657271785e-05 | 43.28% | 76.32% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.177958102933755e-05 | 2.111674192265493e-05 | 49.46% | 97.85% | 1.98x | ✅ |
| `keccak[int]` | 9.327162357714933e-05 | 2.8723742590074487e-05 | 69.20% | 224.72% | 3.25x | ✅ |
| `keccak[text]` | 3.5319810575793754e-05 | 1.9429312192282235e-05 | 44.99% | 81.79% | 1.82x | ✅ |
