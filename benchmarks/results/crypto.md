#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypyc-32bit-no-any-return/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1520786695593546e-05 | 1.6966139595418626e-05 | 46.17% | 85.79% | 1.86x | ✅ |
| `keccak[bytes]` | 3.402057575264541e-05 | 1.9471796889379744e-05 | 42.76% | 74.72% | 1.75x | ✅ |
| `keccak[hexstr]` | 4.1728290607177236e-05 | 2.1389093495818206e-05 | 48.74% | 95.09% | 1.95x | ✅ |
| `keccak[int]` | 9.558292071053503e-05 | 2.05394649158174e-05 | 78.51% | 365.36% | 4.65x | ✅ |
| `keccak[text]` | 3.6310268058248615e-05 | 2.0376531205971015e-05 | 43.88% | 78.20% | 1.78x | ✅ |
