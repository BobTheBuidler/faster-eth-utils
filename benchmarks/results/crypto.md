#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/project-urls/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.847842031914834e-05 | 7.145936061823702e-05 | 19.24% | 23.82% | 1.24x | ✅ |
| `keccak[bytes]` | 9.006080942115371e-05 | 7.34064289633622e-05 | 18.49% | 22.69% | 1.23x | ✅ |
| `keccak[hexstr]` | 0.00010170040421056063 | 7.6436951361923e-05 | 24.84% | 33.05% | 1.33x | ✅ |
| `keccak[int]` | 0.0001578499141133857 | 8.522770134000303e-05 | 46.01% | 85.21% | 1.85x | ✅ |
| `keccak[text]` | 9.226209376919977e-05 | 7.380428725265245e-05 | 20.01% | 25.01% | 1.25x | ✅ |
