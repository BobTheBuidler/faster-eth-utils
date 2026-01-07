#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/is_hex_address/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.120600551364727e-05 | 1.6918946890237215e-05 | 45.78% | 84.44% | 1.84x | ✅ |
| `keccak[bytes]` | 3.319252422385295e-05 | 1.8813710568879613e-05 | 43.32% | 76.43% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.115643955642819e-05 | 2.124049331351719e-05 | 48.39% | 93.76% | 1.94x | ✅ |
| `keccak[int]` | 9.473340089358931e-05 | 2.8362558178350712e-05 | 70.06% | 234.01% | 3.34x | ✅ |
| `keccak[text]` | 3.553927432085102e-05 | 1.9511695655216486e-05 | 45.10% | 82.14% | 1.82x | ✅ |
