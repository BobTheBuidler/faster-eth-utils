#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/eth-hash-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.2308256553327325e-05 | 1.698508414487336e-05 | 47.43% | 90.22% | 1.90x | ✅ |
| `keccak[bytes]` | 3.4151079186405716e-05 | 1.8919548150727167e-05 | 44.60% | 80.51% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.197355024442788e-05 | 2.085498021077133e-05 | 50.31% | 101.26% | 2.01x | ✅ |
| `keccak[int]` | 9.280543194218591e-05 | 2.093337629775062e-05 | 77.44% | 343.34% | 4.43x | ✅ |
| `keccak[text]` | 3.631436195323603e-05 | 1.9522117727736492e-05 | 46.24% | 86.02% | 1.86x | ✅ |
