#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.297145091408786e-05 | 1.767399422546079e-05 | 46.40% | 86.55% | 1.87x | ✅ |
| `keccak[bytes]` | 3.510429586818318e-05 | 1.989923742240771e-05 | 43.31% | 76.41% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.350681782598221e-05 | 2.183235476853007e-05 | 49.82% | 99.28% | 1.99x | ✅ |
| `keccak[int]` | 9.858151756729825e-05 | 2.154884139889727e-05 | 78.14% | 357.48% | 4.57x | ✅ |
| `keccak[text]` | 3.746882600040754e-05 | 2.0445247217568626e-05 | 45.43% | 83.26% | 1.83x | ✅ |
