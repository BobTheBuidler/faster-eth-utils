#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/hex-type-checks/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.215013629963238e-05 | 1.6970877173382617e-05 | 47.21% | 89.44% | 1.89x | ✅ |
| `keccak[bytes]` | 3.426646164992972e-05 | 1.8950153162576653e-05 | 44.70% | 80.82% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.264912065269738e-05 | 2.1627232339101397e-05 | 49.29% | 97.20% | 1.97x | ✅ |
| `keccak[int]` | 9.827521170178958e-05 | 2.8868032115026085e-05 | 70.63% | 240.43% | 3.40x | ✅ |
| `keccak[text]` | 3.646515904659422e-05 | 1.968285012029249e-05 | 46.02% | 85.26% | 1.85x | ✅ |
