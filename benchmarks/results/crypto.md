#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/refactor/logging-assoc-20260126072804/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.125973212618133e-05 | 1.722685149500294e-05 | 44.89% | 81.46% | 1.81x | ✅ |
| `keccak[bytes]` | 3.394590633809921e-05 | 1.9155941224311952e-05 | 43.57% | 77.21% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.1332864925598296e-05 | 2.1292969137750582e-05 | 48.48% | 94.12% | 1.94x | ✅ |
| `keccak[int]` | 9.370106088214549e-05 | 2.0743835533682716e-05 | 77.86% | 351.71% | 4.52x | ✅ |
| `keccak[text]` | 3.579035520457521e-05 | 1.9924281747685767e-05 | 44.33% | 79.63% | 1.80x | ✅ |
