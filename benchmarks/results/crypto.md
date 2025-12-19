#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/bobthebuidler-mypycify-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.143966855062095e-05 | 1.683530076397897e-05 | 46.45% | 86.75% | 1.87x | ✅ |
| `keccak[bytes]` | 3.3316450631104146e-05 | 1.8850835062642188e-05 | 43.42% | 76.74% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.142181422858671e-05 | 2.139447154594227e-05 | 48.35% | 93.61% | 1.94x | ✅ |
| `keccak[int]` | 9.489375992374527e-05 | 2.8779451213644617e-05 | 69.67% | 229.73% | 3.30x | ✅ |
| `keccak[text]` | 3.53869060394757e-05 | 1.9657570471587536e-05 | 44.45% | 80.02% | 1.80x | ✅ |
