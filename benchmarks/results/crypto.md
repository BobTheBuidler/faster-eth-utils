#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/actions-github-script-9.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.3065028408656107e-05 | 1.7743930539879824e-05 | 46.34% | 86.35% | 1.86x | ✅ |
| `keccak[bytes]` | 3.491063089429732e-05 | 1.9588264420671363e-05 | 43.89% | 78.22% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.4202143331145795e-05 | 2.1641504926952817e-05 | 51.04% | 104.25% | 2.04x | ✅ |
| `keccak[int]` | 0.00010044122104148634 | 2.0152335813687736e-05 | 79.94% | 398.41% | 4.98x | ✅ |
| `keccak[text]` | 3.7616036544275236e-05 | 1.9920928632428e-05 | 47.04% | 88.83% | 1.89x | ✅ |
