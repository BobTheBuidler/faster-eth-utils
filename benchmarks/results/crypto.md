#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.305450864146372e-05 | 1.7828919338760842e-05 | 46.06% | 85.40% | 1.85x | ✅ |
| `keccak[bytes]` | 3.4996176012709157e-05 | 1.9512212081812763e-05 | 44.24% | 79.36% | 1.79x | ✅ |
| `keccak[hexstr]` | 4.290255449358817e-05 | 2.228537702307084e-05 | 48.06% | 92.51% | 1.93x | ✅ |
| `keccak[int]` | 9.402215244219358e-05 | 2.0380480873632534e-05 | 78.32% | 361.33% | 4.61x | ✅ |
| `keccak[text]` | 3.76050611979335e-05 | 2.0532017442513223e-05 | 45.40% | 83.15% | 1.83x | ✅ |
