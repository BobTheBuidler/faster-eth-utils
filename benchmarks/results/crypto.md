#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/pytest-benchmark-5.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.103231587968666e-05 | 1.606012234863556e-05 | 48.25% | 93.23% | 1.93x | ✅ |
| `keccak[bytes]` | 3.285753212693309e-05 | 1.7577930705686515e-05 | 46.50% | 86.92% | 1.87x | ✅ |
| `keccak[hexstr]` | 4.1310204941434905e-05 | 1.9629035246122286e-05 | 52.48% | 110.45% | 2.10x | ✅ |
| `keccak[int]` | 9.556725339248084e-05 | 1.845251717500275e-05 | 80.69% | 417.91% | 5.18x | ✅ |
| `keccak[text]` | 3.5202594538843185e-05 | 1.8256272834423093e-05 | 48.14% | 92.82% | 1.93x | ✅ |
