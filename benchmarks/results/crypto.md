#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/pin-eth-utils/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 8.69432231781899e-05 | 7.189228974454637e-05 | 17.31% | 20.94% | 1.21x | ✅ |
| `keccak[bytes]` | 9.055353333072465e-05 | 7.449047743265821e-05 | 17.74% | 21.56% | 1.22x | ✅ |
| `keccak[hexstr]` | 9.933903503494559e-05 | 7.720586634217656e-05 | 22.28% | 28.67% | 1.29x | ✅ |
| `keccak[int]` | 0.00015411901510797353 | 8.606832878349974e-05 | 44.15% | 79.07% | 1.79x | ✅ |
| `keccak[text]` | 9.208854215227036e-05 | 7.488129635672923e-05 | 18.69% | 22.98% | 1.23x | ✅ |
