#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1298069305747804e-05 | 1.6875224269032775e-05 | 46.08% | 85.47% | 1.85x | ✅ |
| `keccak[bytes]` | 3.33516428363596e-05 | 1.889016227824049e-05 | 43.36% | 76.56% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.1462248624373256e-05 | 2.0832243785461507e-05 | 49.76% | 99.03% | 1.99x | ✅ |
| `keccak[int]` | 9.386053920972769e-05 | 2.1111264519614066e-05 | 77.51% | 344.60% | 4.45x | ✅ |
| `keccak[text]` | 3.5444851288810814e-05 | 1.9515498943599742e-05 | 44.94% | 81.62% | 1.82x | ✅ |
