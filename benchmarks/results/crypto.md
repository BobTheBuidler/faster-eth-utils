#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf/int-to-bytes-fast/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.123279773700292e-05 | 1.698096465982472e-05 | 45.63% | 83.93% | 1.84x | ✅ |
| `keccak[bytes]` | 3.3234457275283056e-05 | 1.888188156361877e-05 | 43.19% | 76.01% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.187675721879063e-05 | 2.1128121861736656e-05 | 49.55% | 98.20% | 1.98x | ✅ |
| `keccak[int]` | 9.563639605290357e-05 | 2.0326844231900454e-05 | 78.75% | 370.49% | 4.70x | ✅ |
| `keccak[text]` | 3.567303422043618e-05 | 1.9663271881741683e-05 | 44.88% | 81.42% | 1.81x | ✅ |
