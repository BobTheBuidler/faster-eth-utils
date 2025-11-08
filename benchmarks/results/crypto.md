#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.207942139711926e-05 | 1.675604126948219e-05 | 47.77% | 91.45% | 1.91x | ✅ |
| `keccak[bytes]` | 3.424604376309162e-05 | 1.871289988129753e-05 | 45.36% | 83.01% | 1.83x | ✅ |
| `keccak[hexstr]` | 4.280625554522824e-05 | 2.1178281357408095e-05 | 50.53% | 102.12% | 2.02x | ✅ |
| `keccak[int]` | 9.497688206679492e-05 | 2.883758665963967e-05 | 69.64% | 229.35% | 3.29x | ✅ |
| `keccak[text]` | 3.655037486678061e-05 | 1.939134234909821e-05 | 46.95% | 88.49% | 1.88x | ✅ |
