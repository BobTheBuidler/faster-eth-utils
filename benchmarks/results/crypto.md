#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/perf-encode-hex/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1379598804511725e-05 | 1.7002488688467227e-05 | 45.82% | 84.56% | 1.85x | ✅ |
| `keccak[bytes]` | 3.337819744140162e-05 | 1.8929232886115646e-05 | 43.29% | 76.33% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.1420183093493336e-05 | 2.130487654645351e-05 | 48.56% | 94.42% | 1.94x | ✅ |
| `keccak[int]` | 9.439254421781644e-05 | 2.879378996298506e-05 | 69.50% | 227.82% | 3.28x | ✅ |
| `keccak[text]` | 3.557954387204988e-05 | 1.9559496372855854e-05 | 45.03% | 81.90% | 1.82x | ✅ |
