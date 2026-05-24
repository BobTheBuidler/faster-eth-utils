#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.252930242285459e-05 | 1.7419065102616115e-05 | 46.45% | 86.75% | 1.87x | ✅ |
| `keccak[bytes]` | 3.467773042176627e-05 | 1.918196248576795e-05 | 44.69% | 80.78% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.313169574514022e-05 | 2.1224549523974097e-05 | 50.79% | 103.22% | 2.03x | ✅ |
| `keccak[int]` | 9.739830644693583e-05 | 2.0083041309189797e-05 | 79.38% | 384.98% | 4.85x | ✅ |
| `keccak[text]` | 3.7349154821958806e-05 | 1.963764930665773e-05 | 47.42% | 90.19% | 1.90x | ✅ |
