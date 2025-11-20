#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-checkout-6.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.141404620328246e-05 | 1.685975828458424e-05 | 46.33% | 86.33% | 1.86x | ✅ |
| `keccak[bytes]` | 3.347865492646211e-05 | 1.8762913622366964e-05 | 43.96% | 78.43% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.124002585234694e-05 | 2.0966659437084422e-05 | 49.16% | 96.69% | 1.97x | ✅ |
| `keccak[int]` | 9.209509031979872e-05 | 2.8972331977137152e-05 | 68.54% | 217.87% | 3.18x | ✅ |
| `keccak[text]` | 3.513509328006971e-05 | 1.9256421477992278e-05 | 45.19% | 82.46% | 1.82x | ✅ |
