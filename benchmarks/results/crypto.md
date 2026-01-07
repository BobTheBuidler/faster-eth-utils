#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-5/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1456388376175775e-05 | 1.679680695771956e-05 | 46.60% | 87.28% | 1.87x | ✅ |
| `keccak[bytes]` | 3.3410862608113676e-05 | 1.899059834697715e-05 | 43.16% | 75.93% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.137439047135248e-05 | 2.1197375630099732e-05 | 48.77% | 95.19% | 1.95x | ✅ |
| `keccak[int]` | 9.46802450201576e-05 | 2.863744661479367e-05 | 69.75% | 230.62% | 3.31x | ✅ |
| `keccak[text]` | 3.555643074607914e-05 | 1.9611054657931998e-05 | 44.85% | 81.31% | 1.81x | ✅ |
