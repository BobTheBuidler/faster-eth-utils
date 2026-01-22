#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 2.929510154140809e-05 | 1.5584863552177474e-05 | 46.80% | 87.97% | 1.88x | ✅ |
| `keccak[bytes]` | 3.117306104330014e-05 | 1.7192241283788753e-05 | 44.85% | 81.32% | 1.81x | ✅ |
| `keccak[hexstr]` | 3.867317032569622e-05 | 1.8997067931323975e-05 | 50.88% | 103.57% | 2.04x | ✅ |
| `keccak[int]` | 8.934922007435974e-05 | 1.8935109448232972e-05 | 78.81% | 371.87% | 4.72x | ✅ |
| `keccak[text]` | 3.312801970682707e-05 | 1.781792256801725e-05 | 46.21% | 85.93% | 1.86x | ✅ |
