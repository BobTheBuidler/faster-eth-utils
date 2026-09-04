#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/towncrier-26.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.827420492088405e-05 | 1.4847602032899692e-05 | 47.49% | 90.43% | 1.90x | ✅ |
| `keccak[bytes]` | 2.989090049976449e-05 | 1.6029758684887977e-05 | 46.37% | 86.47% | 1.86x | ✅ |
| `keccak[hexstr]` | 3.6204350819782175e-05 | 1.8231121335013087e-05 | 49.64% | 98.59% | 1.99x | ✅ |
| `keccak[int]` | 8.15488789267711e-05 | 1.6764088936575068e-05 | 79.44% | 386.45% | 4.86x | ✅ |
| `keccak[text]` | 3.1564981608967786e-05 | 1.671360400344459e-05 | 47.05% | 88.86% | 1.89x | ✅ |
