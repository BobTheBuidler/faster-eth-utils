#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.101035659806957e-05 | 1.6781514294288608e-05 | 45.88% | 84.79% | 1.85x | ✅ |
| `keccak[bytes]` | 3.302575406266553e-05 | 1.8591140877588507e-05 | 43.71% | 77.64% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.0941712849520094e-05 | 2.057837051414718e-05 | 49.74% | 98.96% | 1.99x | ✅ |
| `keccak[int]` | 9.42204967237854e-05 | 2.0584533698891397e-05 | 78.15% | 357.72% | 4.58x | ✅ |
| `keccak[text]` | 3.5183174062643055e-05 | 1.9149591155762538e-05 | 45.57% | 83.73% | 1.84x | ✅ |
