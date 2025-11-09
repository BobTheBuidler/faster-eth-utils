#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/fix-sdist/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.168162611860631e-05 | 1.6891323577960885e-05 | 46.68% | 87.56% | 1.88x | ✅ |
| `keccak[bytes]` | 3.3654790009282615e-05 | 1.8945721999362547e-05 | 43.71% | 77.64% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.168895797595319e-05 | 2.1317079918024102e-05 | 48.87% | 95.57% | 1.96x | ✅ |
| `keccak[int]` | 9.565714843851626e-05 | 2.949361459988321e-05 | 69.17% | 224.33% | 3.24x | ✅ |
| `keccak[text]` | 3.5879500512117917e-05 | 1.9397769758599385e-05 | 45.94% | 84.97% | 1.85x | ✅ |
