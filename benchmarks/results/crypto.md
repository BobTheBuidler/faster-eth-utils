#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.133343576287821e-05 | 1.6835113116352955e-05 | 46.27% | 86.12% | 1.86x | ✅ |
| `keccak[bytes]` | 3.3312312489219426e-05 | 1.8367154191373742e-05 | 44.86% | 81.37% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.1211223755757835e-05 | 2.0421293742803088e-05 | 50.45% | 101.81% | 2.02x | ✅ |
| `keccak[int]` | 9.328719759650635e-05 | 1.9697569354739514e-05 | 78.89% | 373.60% | 4.74x | ✅ |
| `keccak[text]` | 3.569789243035192e-05 | 1.905997041131693e-05 | 46.61% | 87.29% | 1.87x | ✅ |
