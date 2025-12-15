#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.9442357243694134e-05 | 1.5224593734247477e-05 | 48.29% | 93.39% | 1.93x | ✅ |
| `keccak[bytes]` | 3.134225934550845e-05 | 1.6989031871662274e-05 | 45.80% | 84.49% | 1.84x | ✅ |
| `keccak[hexstr]` | 3.9194557373406995e-05 | 1.9014688932965968e-05 | 51.49% | 106.13% | 2.06x | ✅ |
| `keccak[int]` | 8.955057852922848e-05 | 2.616190950375441e-05 | 70.79% | 242.29% | 3.42x | ✅ |
| `keccak[text]` | 3.335928615229471e-05 | 1.7634971581498537e-05 | 47.14% | 89.17% | 1.89x | ✅ |
