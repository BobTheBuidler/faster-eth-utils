#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1157401556803413e-05 | 1.6800411318134427e-05 | 46.08% | 85.46% | 1.85x | ✅ |
| `keccak[bytes]` | 3.32838097523781e-05 | 1.879575174304014e-05 | 43.53% | 77.08% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.1228745109761935e-05 | 2.1314549717427746e-05 | 48.30% | 93.43% | 1.93x | ✅ |
| `keccak[int]` | 9.336134393079102e-05 | 2.8406085460646862e-05 | 69.57% | 228.67% | 3.29x | ✅ |
| `keccak[text]` | 3.56123362591355e-05 | 1.9449912126031483e-05 | 45.38% | 83.10% | 1.83x | ✅ |
