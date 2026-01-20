#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.103032195660445e-05 | 1.6916491644294133e-05 | 45.48% | 83.43% | 1.83x | ✅ |
| `keccak[bytes]` | 3.281458331038795e-05 | 1.8982073148599966e-05 | 42.15% | 72.87% | 1.73x | ✅ |
| `keccak[hexstr]` | 4.1026710112274975e-05 | 2.090297220766985e-05 | 49.05% | 96.27% | 1.96x | ✅ |
| `keccak[int]` | 9.296991563902297e-05 | 2.050831154649286e-05 | 77.94% | 353.33% | 4.53x | ✅ |
| `keccak[text]` | 3.525561586749904e-05 | 1.9615130613452648e-05 | 44.36% | 79.74% | 1.80x | ✅ |
