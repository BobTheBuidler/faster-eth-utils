#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/cchecksum-0.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1253251428953965e-05 | 1.6848018068668254e-05 | 46.09% | 85.50% | 1.86x | ✅ |
| `keccak[bytes]` | 3.336053871731225e-05 | 1.8974717894012823e-05 | 43.12% | 75.82% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.1329540498708924e-05 | 2.109590636756106e-05 | 48.96% | 95.91% | 1.96x | ✅ |
| `keccak[int]` | 9.29395821317521e-05 | 2.9998415964849862e-05 | 67.72% | 209.81% | 3.10x | ✅ |
| `keccak[text]` | 3.523132162078142e-05 | 1.9437430624410114e-05 | 44.83% | 81.26% | 1.81x | ✅ |
