#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.117639536356572e-05 | 1.6748601014418713e-05 | 46.28% | 86.14% | 1.86x | ✅ |
| `keccak[bytes]` | 3.309569767041865e-05 | 1.8748225474127437e-05 | 43.35% | 76.53% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.1151150680208124e-05 | 2.126828905043046e-05 | 48.32% | 93.49% | 1.93x | ✅ |
| `keccak[int]` | 9.2653528701543e-05 | 2.7993235542599644e-05 | 69.79% | 230.99% | 3.31x | ✅ |
| `keccak[text]` | 3.490747695260532e-05 | 1.9462022453620487e-05 | 44.25% | 79.36% | 1.79x | ✅ |
