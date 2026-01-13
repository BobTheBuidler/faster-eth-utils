#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-1/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.127452135035722e-05 | 1.6861344142681783e-05 | 46.09% | 85.48% | 1.85x | ✅ |
| `keccak[bytes]` | 3.355092644516006e-05 | 1.8880148401810455e-05 | 43.73% | 77.70% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.14617176611848e-05 | 2.133963640510915e-05 | 48.53% | 94.29% | 1.94x | ✅ |
| `keccak[int]` | 9.391444786979748e-05 | 2.8474421757639774e-05 | 69.68% | 229.82% | 3.30x | ✅ |
| `keccak[text]` | 3.5520893136185776e-05 | 1.975743402350536e-05 | 44.38% | 79.78% | 1.80x | ✅ |
