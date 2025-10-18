#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/runners/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.588587753640289e-05 | 6.82410418841127e-05 | 20.54% | 25.86% | 1.26x | ✅ |
| `keccak[bytes]` | 8.705389893077522e-05 | 7.141723318087944e-05 | 17.96% | 21.89% | 1.22x | ✅ |
| `keccak[hexstr]` | 9.628154401637246e-05 | 7.46831275672805e-05 | 22.43% | 28.92% | 1.29x | ✅ |
| `keccak[int]` | 0.0001573718776437572 | 8.392346782150831e-05 | 46.67% | 87.52% | 1.88x | ✅ |
| `keccak[text]` | 8.955297240705715e-05 | 7.247748284891668e-05 | 19.07% | 23.56% | 1.24x | ✅ |
