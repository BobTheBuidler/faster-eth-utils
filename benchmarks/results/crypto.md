#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/python-3.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.435091409743268e-05 | 6.903396312646718e-05 | 18.16% | 22.19% | 1.22x | ✅ |
| `keccak[bytes]` | 8.6482947679449e-05 | 7.094611278926196e-05 | 17.97% | 21.90% | 1.22x | ✅ |
| `keccak[hexstr]` | 9.595420360617133e-05 | 7.445284828728767e-05 | 22.41% | 28.88% | 1.29x | ✅ |
| `keccak[int]` | 0.00014978121894909514 | 8.33143711387264e-05 | 44.38% | 79.78% | 1.80x | ✅ |
| `keccak[text]` | 8.864483911797839e-05 | 7.219719391102325e-05 | 18.55% | 22.78% | 1.23x | ✅ |
