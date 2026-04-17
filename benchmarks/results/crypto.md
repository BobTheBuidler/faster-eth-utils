#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.096342636579802e-05 | 1.6724602048935415e-05 | 45.99% | 85.14% | 1.85x | ✅ |
| `keccak[bytes]` | 3.315468631470783e-05 | 1.8236505212776575e-05 | 45.00% | 81.80% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.1276545098223276e-05 | 2.026527209959348e-05 | 50.90% | 103.68% | 2.04x | ✅ |
| `keccak[int]` | 9.28160402122751e-05 | 1.8925171944220885e-05 | 79.61% | 390.44% | 4.90x | ✅ |
| `keccak[text]` | 3.542884760164117e-05 | 1.8831641835622055e-05 | 46.85% | 88.13% | 1.88x | ✅ |
