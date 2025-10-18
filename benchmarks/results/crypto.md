#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-4/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.782224512580663e-05 | 7.075086330385473e-05 | 19.44% | 24.13% | 1.24x | ✅ |
| `keccak[bytes]` | 8.879227699995454e-05 | 7.212230954634103e-05 | 18.77% | 23.11% | 1.23x | ✅ |
| `keccak[hexstr]` | 0.00010052060099549443 | 7.759019154474624e-05 | 22.81% | 29.55% | 1.30x | ✅ |
| `keccak[int]` | 0.00015570879371764706 | 8.502462780809715e-05 | 45.40% | 83.13% | 1.83x | ✅ |
| `keccak[text]` | 9.130075136084527e-05 | 7.34670110399383e-05 | 19.53% | 24.27% | 1.24x | ✅ |
