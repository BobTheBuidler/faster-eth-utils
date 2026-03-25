#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-typing-6.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1773543344419176e-05 | 1.680722344794947e-05 | 47.10% | 89.05% | 1.89x | ✅ |
| `keccak[bytes]` | 3.3610532930369375e-05 | 1.883196466725616e-05 | 43.97% | 78.48% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.1164407627577194e-05 | 2.086174770645454e-05 | 49.32% | 97.32% | 1.97x | ✅ |
| `keccak[int]` | 9.30987999745793e-05 | 2.0612725657075494e-05 | 77.86% | 351.66% | 4.52x | ✅ |
| `keccak[text]` | 3.5566932230659154e-05 | 1.947149547417686e-05 | 45.25% | 82.66% | 1.83x | ✅ |
