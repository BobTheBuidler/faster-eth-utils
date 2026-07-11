#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.275681198527485e-05 | 1.823419196472342e-05 | 44.33% | 79.64% | 1.80x | ✅ |
| `keccak[bytes]` | 3.477267449257686e-05 | 1.9509032359440813e-05 | 43.90% | 78.24% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.258862089757874e-05 | 2.1477019595739905e-05 | 49.57% | 98.30% | 1.98x | ✅ |
| `keccak[int]` | 9.310307942746219e-05 | 2.0521738391018328e-05 | 77.96% | 353.68% | 4.54x | ✅ |
| `keccak[text]` | 3.683099481481374e-05 | 2.0153644997512843e-05 | 45.28% | 82.75% | 1.83x | ✅ |
