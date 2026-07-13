#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.253987340360266e-05 | 1.7509315170138558e-05 | 46.19% | 85.84% | 1.86x | ✅ |
| `keccak[bytes]` | 3.478331564571274e-05 | 1.919724881291761e-05 | 44.81% | 81.19% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.341431836624737e-05 | 2.1223464412540583e-05 | 51.11% | 104.56% | 2.05x | ✅ |
| `keccak[int]` | 9.812440632718106e-05 | 2.0006323585864563e-05 | 79.61% | 390.47% | 4.90x | ✅ |
| `keccak[text]` | 3.7538749662818e-05 | 1.9918177031191055e-05 | 46.94% | 88.46% | 1.88x | ✅ |
