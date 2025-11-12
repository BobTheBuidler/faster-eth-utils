#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.262656946160521e-05 | 1.7238658884669667e-05 | 47.16% | 89.26% | 1.89x | ✅ |
| `keccak[bytes]` | 3.492589810973115e-05 | 1.934595387623089e-05 | 44.61% | 80.53% | 1.81x | ✅ |
| `keccak[hexstr]` | 4.294105501831915e-05 | 2.173097233370199e-05 | 49.39% | 97.60% | 1.98x | ✅ |
| `keccak[int]` | 9.584513209978466e-05 | 2.965059579263828e-05 | 69.06% | 223.25% | 3.23x | ✅ |
| `keccak[text]` | 3.686883153690915e-05 | 2.0093362674942553e-05 | 45.50% | 83.49% | 1.83x | ✅ |
