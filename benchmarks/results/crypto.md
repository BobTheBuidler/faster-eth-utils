#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/BobTheBuidler-patch-2/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.116012424405645e-05 | 1.694373577388518e-05 | 45.62% | 83.90% | 1.84x | ✅ |
| `keccak[bytes]` | 3.343067457732832e-05 | 1.894673315495837e-05 | 43.33% | 76.45% | 1.76x | ✅ |
| `keccak[hexstr]` | 4.138514201039058e-05 | 2.1315853033265578e-05 | 48.49% | 94.15% | 1.94x | ✅ |
| `keccak[int]` | 9.443605716409273e-05 | 2.874125001094451e-05 | 69.57% | 228.57% | 3.29x | ✅ |
| `keccak[text]` | 3.580265887697502e-05 | 1.96781204723921e-05 | 45.04% | 81.94% | 1.82x | ✅ |
