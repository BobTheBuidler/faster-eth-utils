#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-2.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1937440241540016e-05 | 1.7438381846371445e-05 | 45.40% | 83.14% | 1.83x | ✅ |
| `keccak[bytes]` | 3.426340796760793e-05 | 1.8998721786787674e-05 | 44.55% | 80.35% | 1.80x | ✅ |
| `keccak[hexstr]` | 4.2340512565268215e-05 | 2.110343706502945e-05 | 50.16% | 100.63% | 2.01x | ✅ |
| `keccak[int]` | 9.446992314829741e-05 | 2.000310042137606e-05 | 78.83% | 372.28% | 4.72x | ✅ |
| `keccak[text]` | 3.633951282669145e-05 | 1.9873538399374194e-05 | 45.31% | 82.85% | 1.83x | ✅ |
