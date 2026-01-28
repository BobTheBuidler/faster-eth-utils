#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1246686043340896e-05 | 1.6828643400532558e-05 | 46.14% | 85.68% | 1.86x | ✅ |
| `keccak[bytes]` | 3.3262956432541565e-05 | 1.8914561854184084e-05 | 43.14% | 75.86% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.128309638849432e-05 | 2.0985254337710435e-05 | 49.17% | 96.72% | 1.97x | ✅ |
| `keccak[int]` | 9.396059111263574e-05 | 2.0471415314109297e-05 | 78.21% | 358.98% | 4.59x | ✅ |
| `keccak[text]` | 3.5816525045999764e-05 | 1.957491745716513e-05 | 45.35% | 82.97% | 1.83x | ✅ |
