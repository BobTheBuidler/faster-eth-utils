#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-codspeed-4.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1987267891036635e-05 | 1.7301800493579072e-05 | 45.91% | 84.88% | 1.85x | ✅ |
| `keccak[bytes]` | 3.397445901459373e-05 | 1.868677669183959e-05 | 45.00% | 81.81% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.2022364031445604e-05 | 2.094723586294234e-05 | 50.15% | 100.61% | 2.01x | ✅ |
| `keccak[int]` | 9.505878675559356e-05 | 1.9581403083230488e-05 | 79.40% | 385.45% | 4.85x | ✅ |
| `keccak[text]` | 3.625031753945122e-05 | 1.9471494293227714e-05 | 46.29% | 86.17% | 1.86x | ✅ |
