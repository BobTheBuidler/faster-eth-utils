#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.312288967202527e-05 | 1.7899436355052432e-05 | 45.96% | 85.05% | 1.85x | ✅ |
| `keccak[bytes]` | 3.5386024325589153e-05 | 1.9490800335490783e-05 | 44.92% | 81.55% | 1.82x | ✅ |
| `keccak[hexstr]` | 4.3146671778861065e-05 | 2.1579578244685117e-05 | 49.99% | 99.94% | 2.00x | ✅ |
| `keccak[int]` | 9.490666532158957e-05 | 2.0481918991823123e-05 | 78.42% | 363.37% | 4.63x | ✅ |
| `keccak[text]` | 3.723139197197934e-05 | 2.0128974724364178e-05 | 45.94% | 84.96% | 1.85x | ✅ |
