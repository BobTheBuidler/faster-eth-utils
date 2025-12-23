#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pyup/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.9266893249157303e-05 | 1.5543722142851654e-05 | 46.89% | 88.29% | 1.88x | ✅ |
| `keccak[bytes]` | 3.108803718981399e-05 | 1.758302861767673e-05 | 43.44% | 76.81% | 1.77x | ✅ |
| `keccak[hexstr]` | 3.9321916405215254e-05 | 2.01198473878676e-05 | 48.83% | 95.44% | 1.95x | ✅ |
| `keccak[int]` | 8.887993020520927e-05 | 2.7024994396277537e-05 | 69.59% | 228.88% | 3.29x | ✅ |
| `keccak[text]` | 3.345643725717123e-05 | 1.8118259950972516e-05 | 45.85% | 84.66% | 1.85x | ✅ |
