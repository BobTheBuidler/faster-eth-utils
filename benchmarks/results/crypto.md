#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/lazy-imports-init/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.2242039699101435e-05 | 1.7011655531245273e-05 | 47.24% | 89.53% | 1.90x | ✅ |
| `keccak[bytes]` | 3.386807345691121e-05 | 1.8975405019541895e-05 | 43.97% | 78.48% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.207169267361994e-05 | 2.1193187293810034e-05 | 49.63% | 98.52% | 1.99x | ✅ |
| `keccak[int]` | 9.621784687484335e-05 | 2.857959818384491e-05 | 70.30% | 236.67% | 3.37x | ✅ |
| `keccak[text]` | 3.6189970554631416e-05 | 1.9518953969597787e-05 | 46.07% | 85.41% | 1.85x | ✅ |
