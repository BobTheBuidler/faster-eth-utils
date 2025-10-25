#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/major-github-artifact-actions/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.572482655944634e-05 | 6.883832771100028e-05 | 19.70% | 24.53% | 1.25x | ✅ |
| `keccak[bytes]` | 8.737328290411914e-05 | 7.07703184765383e-05 | 19.00% | 23.46% | 1.23x | ✅ |
| `keccak[hexstr]` | 9.804993164328614e-05 | 7.560828173608276e-05 | 22.89% | 29.68% | 1.30x | ✅ |
| `keccak[int]` | 0.0001595969398517589 | 8.343568167211236e-05 | 47.72% | 91.28% | 1.91x | ✅ |
| `keccak[text]` | 9.019484039061862e-05 | 7.185233746865465e-05 | 20.34% | 25.53% | 1.26x | ✅ |
