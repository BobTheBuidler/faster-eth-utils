#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.295154599991221e-05 | 1.75915249264513e-05 | 46.61% | 87.31% | 1.87x | ✅ |
| `keccak[bytes]` | 3.500517342645615e-05 | 1.940059560326122e-05 | 44.58% | 80.43% | 1.80x | ✅ |
| `keccak[hexstr]` | 4.343326054185379e-05 | 2.1473488457381885e-05 | 50.56% | 102.26% | 2.02x | ✅ |
| `keccak[int]` | 9.605270163243128e-05 | 2.0321403812476656e-05 | 78.84% | 372.67% | 4.73x | ✅ |
| `keccak[text]` | 3.744235832439241e-05 | 2.014070355250845e-05 | 46.21% | 85.90% | 1.86x | ✅ |
