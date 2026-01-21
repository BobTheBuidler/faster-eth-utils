#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.170982403638446e-05 | 1.687658331079673e-05 | 46.78% | 87.89% | 1.88x | ✅ |
| `keccak[bytes]` | 3.3373730550117444e-05 | 1.8987187201251137e-05 | 43.11% | 75.77% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.171654206117673e-05 | 2.100840562700863e-05 | 49.64% | 98.57% | 1.99x | ✅ |
| `keccak[int]` | 9.428286284329332e-05 | 2.0524632029679805e-05 | 78.23% | 359.36% | 4.59x | ✅ |
| `keccak[text]` | 3.561055106331342e-05 | 1.9571690239395902e-05 | 45.04% | 81.95% | 1.82x | ✅ |
