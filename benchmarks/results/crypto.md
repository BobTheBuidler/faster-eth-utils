#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/codex/evaluate-functions-for-microoptimizations/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.10491380094476e-05 | 1.6990807020408662e-05 | 45.28% | 82.74% | 1.83x | ✅ |
| `keccak[bytes]` | 3.36194168662113e-05 | 1.8891047245591268e-05 | 43.81% | 77.96% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.151625215421648e-05 | 2.1325755124771333e-05 | 48.63% | 94.68% | 1.95x | ✅ |
| `keccak[int]` | 9.411806156722777e-05 | 2.8902119417540403e-05 | 69.29% | 225.64% | 3.26x | ✅ |
| `keccak[text]` | 3.5727163145419244e-05 | 1.951042472136656e-05 | 45.39% | 83.12% | 1.83x | ✅ |
