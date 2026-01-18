#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix/mypy-redundant-cast-type-inference/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1202925808057574e-05 | 1.6642356105728805e-05 | 46.66% | 87.49% | 1.87x | ✅ |
| `keccak[bytes]` | 3.323705801699364e-05 | 1.8903091063686748e-05 | 43.13% | 75.83% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.1072040849143054e-05 | 2.1059672281597392e-05 | 48.73% | 95.03% | 1.95x | ✅ |
| `keccak[int]` | 9.54439961796129e-05 | 2.043787549866636e-05 | 78.59% | 367.00% | 4.67x | ✅ |
| `keccak[text]` | 3.5658399542883604e-05 | 1.9401420591012355e-05 | 45.59% | 83.79% | 1.84x | ✅ |
