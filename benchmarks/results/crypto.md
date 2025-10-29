#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-typing/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.576817806346004e-05 | 6.967872080775365e-05 | 18.76% | 23.09% | 1.23x | ✅ |
| `keccak[bytes]` | 8.758047280967914e-05 | 7.219543126973434e-05 | 17.57% | 21.31% | 1.21x | ✅ |
| `keccak[hexstr]` | 9.768356338256553e-05 | 7.501868322482924e-05 | 23.20% | 30.21% | 1.30x | ✅ |
| `keccak[int]` | 0.00014997955981478492 | 8.706125604951603e-05 | 41.95% | 72.27% | 1.72x | ✅ |
| `keccak[text]` | 9.091460554831148e-05 | 7.283084825127593e-05 | 19.89% | 24.83% | 1.25x | ✅ |
