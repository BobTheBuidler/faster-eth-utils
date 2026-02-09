#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.139557930921236e-05 | 1.6849053204002365e-05 | 46.33% | 86.33% | 1.86x | ✅ |
| `keccak[bytes]` | 3.315960740567538e-05 | 1.8592660372282615e-05 | 43.93% | 78.35% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.188967767729265e-05 | 2.0786714645046073e-05 | 50.38% | 101.52% | 2.02x | ✅ |
| `keccak[int]` | 9.317937289792632e-05 | 2.018282709327603e-05 | 78.34% | 361.68% | 4.62x | ✅ |
| `keccak[text]` | 3.555158184610703e-05 | 1.9211376640021407e-05 | 45.96% | 85.05% | 1.85x | ✅ |
