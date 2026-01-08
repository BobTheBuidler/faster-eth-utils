#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1616699621443864e-05 | 1.6962879617494912e-05 | 46.35% | 86.39% | 1.86x | ✅ |
| `keccak[bytes]` | 3.353798413117602e-05 | 1.8824075823564202e-05 | 43.87% | 78.17% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.1630234217933005e-05 | 2.1142950715449117e-05 | 49.21% | 96.90% | 1.97x | ✅ |
| `keccak[int]` | 9.381180283430956e-05 | 2.8435718187467824e-05 | 69.69% | 229.91% | 3.30x | ✅ |
| `keccak[text]` | 3.583947803707379e-05 | 1.9383022988644416e-05 | 45.92% | 84.90% | 1.85x | ✅ |
