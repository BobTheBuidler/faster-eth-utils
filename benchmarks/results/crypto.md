#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.208159481042101e-05 | 1.7275495033132064e-05 | 46.15% | 85.71% | 1.86x | ✅ |
| `keccak[bytes]` | 3.382152306651825e-05 | 1.9003629988099032e-05 | 43.81% | 77.97% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.2138301495432734e-05 | 2.1073301583172033e-05 | 49.99% | 99.96% | 2.00x | ✅ |
| `keccak[int]` | 9.45515142851556e-05 | 1.986475879487087e-05 | 78.99% | 375.98% | 4.76x | ✅ |
| `keccak[text]` | 3.6202492145164983e-05 | 1.9569593840283213e-05 | 45.94% | 84.99% | 1.85x | ✅ |
