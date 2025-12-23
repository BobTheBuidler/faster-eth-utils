#### [faster_eth_utils.crypto](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/faster_eth_utils/crypto.py) - [view benchmarks](https://github.com/BobTheBuidler/faster-eth-utils/blob/autoflake/benchmarks/test_crypto_benchmarks.py)

| Function | Reference Mean | Faster Mean | % Change | Speedup (%) | x Faster | Faster |
|----------|---------------|-------------|----------|-------------|----------|--------|
| `keccak[bool]` | 3.1444542472578555e-05 | 1.6788457880076498e-05 | 46.61% | 87.30% | 1.87x | ✅ |
| `keccak[bytes]` | 3.353185198883659e-05 | 1.8889888049913525e-05 | 43.67% | 77.51% | 1.78x | ✅ |
| `keccak[hexstr]` | 4.163436590993364e-05 | 2.1245612564261465e-05 | 48.97% | 95.97% | 1.96x | ✅ |
| `keccak[int]` | 9.506486892301931e-05 | 2.8641597828092808e-05 | 69.87% | 231.91% | 3.32x | ✅ |
| `keccak[text]` | 3.5873083179653066e-05 | 1.9607524900090685e-05 | 45.34% | 82.96% | 1.83x | ✅ |
