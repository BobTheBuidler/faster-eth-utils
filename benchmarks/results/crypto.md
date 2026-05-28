#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.2513407165448715e-05 | 1.7307135957872085e-05 | 46.77% | 87.86% | 1.88x | ✅ |
| `keccak[bytes]` | 3.461793922288795e-05 | 1.9003352261534152e-05 | 45.11% | 82.17% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.249027201081145e-05 | 2.1076915907833246e-05 | 50.40% | 101.60% | 2.02x | ✅ |
| `keccak[int]` | 9.640755312215019e-05 | 1.9956422379670797e-05 | 79.30% | 383.09% | 4.83x | ✅ |
| `keccak[text]` | 3.654905837363542e-05 | 1.9702294199579133e-05 | 46.09% | 85.51% | 1.86x | ✅ |
