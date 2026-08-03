#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/codspeedhq-action-5.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.20878470075018e-05 | 1.7221056506850407e-05 | 46.33% | 86.33% | 1.86x | ✅ |
| `keccak[bytes]` | 3.41394548769272e-05 | 1.8798429187424317e-05 | 44.94% | 81.61% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.216351451993195e-05 | 2.0627715316097605e-05 | 51.08% | 104.40% | 2.04x | ✅ |
| `keccak[int]` | 9.55558897749062e-05 | 1.966862510111554e-05 | 79.42% | 385.83% | 4.86x | ✅ |
| `keccak[text]` | 3.623081478446343e-05 | 1.948402492459577e-05 | 46.22% | 85.95% | 1.86x | ✅ |
