#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.153879131967131e-05 | 1.6577291882971444e-05 | 47.44% | 90.25% | 1.90x | ✅ |
| `keccak[bytes]` | 3.27095506190474e-05 | 1.8065639394686825e-05 | 44.77% | 81.06% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.0950186656963356e-05 | 2.0055289800264847e-05 | 51.03% | 104.19% | 2.04x | ✅ |
| `keccak[int]` | 9.2792930735107e-05 | 1.9251735630087335e-05 | 79.25% | 382.00% | 4.82x | ✅ |
| `keccak[text]` | 3.480776344646121e-05 | 1.8677967886497784e-05 | 46.34% | 86.36% | 1.86x | ✅ |
