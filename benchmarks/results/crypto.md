#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1880805066648735e-05 | 1.715811477204305e-05 | 46.18% | 85.81% | 1.86x | ✅ |
| `keccak[bytes]` | 3.394505239291924e-05 | 1.8724964137504394e-05 | 44.84% | 81.28% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.185553905431499e-05 | 2.0990649103958992e-05 | 49.85% | 99.40% | 1.99x | ✅ |
| `keccak[int]` | 9.551938555598418e-05 | 1.9687074381259215e-05 | 79.39% | 385.19% | 4.85x | ✅ |
| `keccak[text]` | 3.6224019510722056e-05 | 1.9530383486395296e-05 | 46.08% | 85.48% | 1.85x | ✅ |
