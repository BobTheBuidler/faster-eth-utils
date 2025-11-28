#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/renovate/mypy-1.x/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1696418991495636e-05 | 1.6828249704824067e-05 | 46.91% | 88.35% | 1.88x | ✅ |
| `keccak[bytes]` | 3.3315473180303854e-05 | 1.88420497755515e-05 | 43.44% | 76.81% | 1.77x | ✅ |
| `keccak[hexstr]` | 4.169212445268807e-05 | 2.1425419946507055e-05 | 48.61% | 94.59% | 1.95x | ✅ |
| `keccak[int]` | 9.353582628177564e-05 | 2.8090514559876608e-05 | 69.97% | 232.98% | 3.33x | ✅ |
| `keccak[text]` | 3.5546261018430335e-05 | 1.9467889560737512e-05 | 45.23% | 82.59% | 1.83x | ✅ |
