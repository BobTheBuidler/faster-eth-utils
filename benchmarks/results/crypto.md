#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/ishexstr/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.9579393273839275e-05 | 1.5453289850492172e-05 | 47.76% | 91.41% | 1.91x | ✅ |
| `keccak[bytes]` | 3.1628852009488815e-05 | 1.721594732429144e-05 | 45.57% | 83.72% | 1.84x | ✅ |
| `keccak[hexstr]` | 3.948041611711679e-05 | 1.9753562625597362e-05 | 49.97% | 99.86% | 2.00x | ✅ |
| `keccak[int]` | 9.023514725484103e-05 | 2.6955638097276137e-05 | 70.13% | 234.75% | 3.35x | ✅ |
| `keccak[text]` | 3.3672424725952744e-05 | 1.799900118468874e-05 | 46.55% | 87.08% | 1.87x | ✅ |
