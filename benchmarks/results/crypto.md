#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/startswith-literals/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.105794664951761e-05 | 1.674190757646822e-05 | 46.09% | 85.51% | 1.86x | ✅ |
| `keccak[bytes]` | 3.306280348606271e-05 | 1.8643363493493976e-05 | 43.61% | 77.34% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.121473178520717e-05 | 2.0740300760672387e-05 | 49.68% | 98.72% | 1.99x | ✅ |
| `keccak[int]` | 9.481702074372924e-05 | 2.7803599646068546e-05 | 70.68% | 241.02% | 3.41x | ✅ |
| `keccak[text]` | 3.591456985442069e-05 | 1.9275672542247277e-05 | 46.33% | 86.32% | 1.86x | ✅ |
